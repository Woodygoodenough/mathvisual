import json
import argparse
import os

def json_to_markdown(json_path, output_md_path):
    """
    Reads a JSON file of exam questions and generates a Markdown file.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    md_content = "# Exam Questions\n\n"

    for q in questions:
        md_content += f"### {q['id']}. {q['text']}\n\n"

        if q.get('graph') and q['graph'].get('output_path'):
            # Provide the path relative to the markdown file
            md_content += f"![Graph for Question {q['id']}]({q['graph']['output_path']})\n\n"

        if 'choices' in q and q['choices']:
            for key, val in q['choices'].items():
                # Mark the correct answer if it's known
                is_correct = " (Correct Answer)" if q.get('answer') == key else ""
                md_content += f"- **{key}**: {val}{is_correct}\n"

        md_content += "\n---\n\n"

    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Exam JSON to Markdown.")
    parser.add_argument("input_json", help="Path to input JSON file.")
    parser.add_argument("output_md", help="Path to output Markdown file.")
    args = parser.parse_args()

    json_to_markdown(args.input_json, args.output_md)
    print(f"Successfully generated {args.output_md}")
