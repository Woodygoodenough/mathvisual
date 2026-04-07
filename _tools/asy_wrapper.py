import os
import json
import subprocess
import tempfile
import argparse

def generate_asy_from_graph_dict(graph_data):
    """
    Generates Asymptote code from a semantic graph dictionary.
    """
    asy_lines = []

    asy_lines.append("size(800, 800);")
    asy_lines.append("defaultpen(linewidth(0.8));")

    # 1. Define points
    points = graph_data.get("points", {})
    for name, coords in points.items():
        asy_lines.append(f"pair {name} = ({coords[0]}, {coords[1]});")

    # 2. Draw lines
    for line in graph_data.get("lines", []):
        pts = line["points"]
        path = "--".join(pts)
        style = line.get("style", "solid")
        if style == "dashed":
            asy_lines.append(f"draw({path}, dashed);")
        else:
            asy_lines.append(f"draw({path});")

    # 3. Add labels with native direction strings
    for label in graph_data.get("labels", []):
        point = label["point"]
        text = label["text"]
        position = label.get("position", "N")
        asy_lines.append(f"label(\"${text}$\", {point}, {position});")

    # 4. Draw right angles in isolated blocks
    for angle in graph_data.get("right_angles", []):
        p1 = angle["p1"]
        p2 = angle["p2"]
        p3 = angle["p3"]
        size = angle.get("size", 0.1)

        asy_lines.append("{")
        asy_lines.append(f"    pair vec1 = unit({p1} - {p2});")
        asy_lines.append(f"    pair vec2 = unit({p3} - {p2});")
        asy_lines.append(f"    pair pt1 = {p2} + {size}*vec1;")
        asy_lines.append(f"    pair pt2 = {p2} + {size}*vec2;")
        asy_lines.append(f"    pair corner = {p2} + {size}*vec1 + {size}*vec2;")
        asy_lines.append(f"    draw(pt1--corner--pt2);")
        asy_lines.append("}")

    # 5. Add line annotations (e.g. lengths)
    for ann in graph_data.get("annotations", []):
        p1 = ann["p1"]
        p2 = ann["p2"]
        text = ann["text"]
        position = ann.get("position", "N")

        asy_lines.append("{")
        asy_lines.append(f"    pair mid = ({p1} + {p2}) / 2.0;")
        asy_lines.append(f"    label(\"{text}\", mid, {position});")
        asy_lines.append("}")

    return "\n".join(asy_lines)

def compile_asy_to_svg(asy_code: str, output_path: str) -> bool:
    """
    Compiles Asymptote code to an SVG file.
    """
    with tempfile.NamedTemporaryFile(suffix='.asy', delete=False, mode='w') as tmp:
        tmp.write(asy_code)
        tmp_path = tmp.name

    try:
        output_base = os.path.splitext(output_path)[0]
        result = subprocess.run(
            ['asy', '-f', 'svg', '-o', output_base, tmp_path],
            check=True,
            capture_output=True,
            text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error compiling Asymptote code:\n{e.stderr}")
        return False
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

def process_exam_json(json_path):
    """
    Reads exam JSON, finds graphs, generates Asymptote code, compiles to SVG.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    base_dir = os.path.dirname(json_path)

    for q in questions:
        if q.get("graph"):
            print(f"Processing graph for question {q['id']}...")
            graph_data = q["graph"]
            asy_code = generate_asy_from_graph_dict(graph_data)

            asy_path = os.path.join(base_dir, f"graph_{q['id']}.asy")
            with open(asy_path, "w") as f:
                f.write(asy_code)

            output_filename = graph_data.get("output_path", f"graph_{q['id']}.svg")
            output_path = os.path.join(base_dir, output_filename)

            compile_asy_to_svg(asy_code, output_path)
            print(f"Generated {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate SVGs from Exam JSON.")
    parser.add_argument("input_json", help="Path to input JSON file.")
    args = parser.parse_args()
    process_exam_json(args.input_json)
