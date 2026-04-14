from pathlib import Path
import ast

MAX_LINES = 200  # safe limit

def split_large_content(content, start_line):
    lines = content.splitlines()
    chunks = []

    for i in range(0, len(lines), MAX_LINES):
        sub_lines = lines[i:i+MAX_LINES]
        chunks.append({
            "content": "\n".join(sub_lines),
            "start_line": start_line + i,
            "end_line": start_line + i + len(sub_lines)
        })

    return chunks


def parse_python_file(file_path: str):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    tree = ast.parse(code)
    chunks = []

    lines = code.splitlines()

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            end_line = getattr(node, "end_lineno", node.lineno)

            content = "\n".join(lines[node.lineno-1:end_line])

            # 🔥 split if too large
            sub_chunks = split_large_content(content, node.lineno)

            for sub in sub_chunks:
                chunks.append({
                    "type": "function" if isinstance(node, ast.FunctionDef) else "class",
                    "name": node.name,
                    "start_line": sub["start_line"],
                    "end_line": sub["end_line"],
                    "content": sub["content"]
                })

    return chunks