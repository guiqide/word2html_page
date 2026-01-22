#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Word to HTML Converter
用于将Word文档转换为HTML格式，特别适用于腾讯游戏的法务条款文档

Word to HTML Converter
For converting Word documents to HTML format, specifically for Tencent Games legal terms
"""

import os
import sys
import argparse
import mammoth
from pathlib import Path


def convert_docx_to_html(input_file, output_file=None, custom_styles=None):
    """
    将.docx文件转换为HTML格式
    Convert .docx file to HTML format
    
    Args:
        input_file (str): 输入的.docx文件路径 / Path to input .docx file
        output_file (str): 输出的HTML文件路径（可选）/ Path to output HTML file (optional)
        custom_styles (dict): 自定义样式映射（可选）/ Custom style mapping (optional)
    
    Returns:
        tuple: (html内容, 消息列表) / (HTML content, list of messages)
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"文件不存在 / File not found: {input_file}")
    
    if not input_path.suffix.lower() in ['.docx']:
        raise ValueError(f"仅支持.docx格式 / Only .docx format is supported: {input_file}")
    
    # 如果没有指定输出文件，使用同名的.html文件
    # If output file is not specified, use the same name with .html extension
    if output_file is None:
        output_file = input_path.with_suffix('.html')
    
    output_path = Path(output_file)
    
    # 确保输出目录存在
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 读取docx文件并转换
    # Read docx file and convert
    with open(input_path, "rb") as docx_file:
        if custom_styles:
            result = mammoth.convert_to_html(docx_file, style_map=custom_styles)
        else:
            result = mammoth.convert_to_html(docx_file)
    
    # 创建完整的HTML页面
    # Create complete HTML page
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{input_path.stem}</title>
    <style>
        body {{
            font-family: "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }}
        p {{
            margin: 0.5em 0;
        }}
        ul, ol {{
            margin: 0.5em 0;
            padding-left: 2em;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }}
        table, th, td {{
            border: 1px solid #ddd;
        }}
        th, td {{
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        strong {{
            font-weight: bold;
        }}
        em {{
            font-style: italic;
        }}
    </style>
</head>
<body>
{result.value}
</body>
</html>
"""
    
    # 写入HTML文件
    # Write HTML file
    with open(output_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    
    return html_content, result.messages, str(output_path)


def main():
    """命令行入口 / Command line entry point"""
    parser = argparse.ArgumentParser(
        description='Word文档转HTML工具 / Word to HTML Converter',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例 / Examples:
  python word2html.py input.docx
  python word2html.py input.docx -o output.html
  python word2html.py input.docx --output-dir ./html_output
        """
    )
    
    parser.add_argument('input', help='输入的.docx文件路径 / Path to input .docx file')
    parser.add_argument('-o', '--output', help='输出的HTML文件路径 / Path to output HTML file')
    parser.add_argument('--output-dir', help='输出目录 / Output directory')
    
    args = parser.parse_args()
    
    try:
        # 处理输出路径
        # Handle output path
        output_file = args.output
        if args.output_dir:
            output_dir = Path(args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            input_name = Path(args.input).stem
            output_file = output_dir / f"{input_name}.html"
        
        # 转换文件
        # Convert file
        print(f"正在转换 / Converting: {args.input}")
        html_content, messages, output_path = convert_docx_to_html(args.input, output_file)
        
        print(f"✓ 转换成功 / Conversion successful!")
        print(f"  输出文件 / Output file: {output_path}")
        
        # 显示警告消息（如果有）
        # Display warning messages (if any)
        if messages:
            print("\n警告 / Warnings:")
            for message in messages:
                print(f"  - {message}")
        
        return 0
        
    except FileNotFoundError as e:
        print(f"✗ 错误 / Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"✗ 错误 / Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"✗ 未预期的错误 / Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
