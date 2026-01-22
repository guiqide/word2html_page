# Word to HTML Converter / Word转HTML转换器

用于将Word文档(.docx)转换为HTML格式的工具，特别适用于腾讯游戏的法务条款文档。

A tool for converting Word documents (.docx) to HTML format, specifically designed for Tencent Games legal terms documents.

## Features / 功能特性

- 📄 支持.docx格式文档转换 / Support .docx format conversion
- 🎨 自动生成带样式的HTML页面 / Automatically generate styled HTML pages
- 🌏 中英文双语支持 / Bilingual support (Chinese & English)
- 🔧 简单易用的命令行工具 / Easy-to-use command-line tool
- 📱 响应式HTML输出 / Responsive HTML output

## Installation / 安装

### Prerequisites / 前置要求

- Python 3.6 或更高版本 / Python 3.6 or higher

### Install Dependencies / 安装依赖

```bash
pip install -r requirements.txt
```

## Usage / 使用方法

### Basic Usage / 基本用法

```bash
# 转换文档（输出同名.html文件）
# Convert document (output to same-name .html file)
python word2html.py input.docx

# 指定输出文件
# Specify output file
python word2html.py input.docx -o output.html

# 指定输出目录
# Specify output directory
python word2html.py input.docx --output-dir ./html_output
```

### Command Line Options / 命令行选项

```
usage: word2html.py [-h] [-o OUTPUT] [--output-dir OUTPUT_DIR] input

positional arguments:
  input                 输入的.docx文件路径 / Path to input .docx file

optional arguments:
  -h, --help            显示帮助信息 / Show help message
  -o OUTPUT, --output OUTPUT
                        输出的HTML文件路径 / Path to output HTML file
  --output-dir OUTPUT_DIR
                        输出目录 / Output directory
```

### Python API / Python API 使用

```python
from word2html import convert_docx_to_html

# 转换文档
# Convert document
html_content, messages, output_path = convert_docx_to_html(
    input_file='input.docx',
    output_file='output.html'
)

print(f"Generated: {output_path}")
```

## Output Format / 输出格式

转换后的HTML文件包含：
The converted HTML file includes:

- 完整的HTML5文档结构 / Complete HTML5 document structure
- 响应式设计样式 / Responsive design styles
- 适合中文阅读的字体设置 / Font settings optimized for Chinese reading
- 表格、列表、标题等格式保留 / Preserved formatting for tables, lists, headings, etc.

## Use Cases / 使用场景

- 📜 法务条款文档转换 / Legal terms document conversion
- 📋 协议文档网页化 / Agreement document web publishing
- 📝 政策文档发布 / Policy document publishing
- 📄 任何需要将Word文档转为网页的场景 / Any scenario requiring Word to web conversion

## Technical Details / 技术细节

本工具使用以下技术：
This tool uses the following technologies:

- **mammoth**: 用于.docx到HTML的核心转换 / Core conversion from .docx to HTML
- **python-docx**: 用于文档处理支持 / Document processing support

## License / 许可证

MIT License

## Support / 支持

如有问题或建议，请提交Issue。
For issues or suggestions, please submit an Issue.