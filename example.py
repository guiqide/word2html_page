#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例脚本：展示如何使用word2html转换器
Example script: Demonstrates how to use the word2html converter
"""

from word2html import convert_docx_to_html
from pathlib import Path


def create_sample_usage_example():
    """
    创建示例用法
    Create sample usage example
    """
    print("=" * 60)
    print("Word to HTML Converter - 使用示例 / Usage Example")
    print("=" * 60)
    print()
    
    # 示例1：基本转换
    # Example 1: Basic conversion
    print("示例 1 / Example 1: 基本转换 / Basic conversion")
    print("-" * 60)
    print("代码 / Code:")
    print("""
from word2html import convert_docx_to_html

html_content, messages, output_path = convert_docx_to_html(
    input_file='legal_terms.docx'
)
print(f"转换成功！/ Conversion successful!")
print(f"输出文件 / Output file: {output_path}")
    """)
    print()
    
    # 示例2：指定输出文件
    # Example 2: Specify output file
    print("示例 2 / Example 2: 指定输出文件 / Specify output file")
    print("-" * 60)
    print("代码 / Code:")
    print("""
from word2html import convert_docx_to_html

html_content, messages, output_path = convert_docx_to_html(
    input_file='legal_terms.docx',
    output_file='output/tencent_legal_terms.html'
)
print(f"输出文件 / Output file: {output_path}")
    """)
    print()
    
    # 示例3：批量转换
    # Example 3: Batch conversion
    print("示例 3 / Example 3: 批量转换多个文件 / Batch conversion")
    print("-" * 60)
    print("代码 / Code:")
    print("""
from word2html import convert_docx_to_html
from pathlib import Path

# 获取所有docx文件 / Get all docx files
docx_files = Path('./documents').glob('*.docx')

for docx_file in docx_files:
    try:
        html_content, messages, output_path = convert_docx_to_html(
            input_file=str(docx_file),
            output_file=f'output/{docx_file.stem}.html'
        )
        print(f"✓ 已转换 / Converted: {docx_file.name}")
    except Exception as e:
        print(f"✗ 转换失败 / Failed: {docx_file.name} - {e}")
    """)
    print()
    
    # 命令行示例
    # Command line examples
    print("命令行示例 / Command Line Examples")
    print("=" * 60)
    print()
    print("# 基本用法 / Basic usage:")
    print("python word2html.py legal_terms.docx")
    print()
    print("# 指定输出文件 / Specify output file:")
    print("python word2html.py legal_terms.docx -o tencent_terms.html")
    print()
    print("# 指定输出目录 / Specify output directory:")
    print("python word2html.py legal_terms.docx --output-dir ./output")
    print()
    
    # 特点说明
    # Feature highlights
    print("主要特点 / Key Features")
    print("=" * 60)
    print("✓ 自动生成完整HTML页面 / Automatically generates complete HTML page")
    print("✓ 内置中文优化样式 / Built-in Chinese-optimized styles")
    print("✓ 保留文档格式 / Preserves document formatting")
    print("✓ 支持表格、列表、标题 / Supports tables, lists, headings")
    print("✓ 响应式设计 / Responsive design")
    print()


if __name__ == "__main__":
    create_sample_usage_example()
