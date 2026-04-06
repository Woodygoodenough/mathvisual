import os
import subprocess
import tempfile

def compile_asy_to_svg(asy_code: str, output_path: str) -> bool:
    """
    Compiles Asymptote code to an SVG file.

    Args:
        asy_code (str): The raw Asymptote code.
        output_path (str): The path where the generated SVG should be saved.

    Returns:
        bool: True if compilation was successful, False otherwise.
    """
    with tempfile.NamedTemporaryFile(suffix='.asy', delete=False, mode='w') as tmp:
        tmp.write(asy_code)
        tmp_path = tmp.name

    try:
        # Run asymptote: asy -f svg -o <output_path_without_ext> <input_file>
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

if __name__ == "__main__":
    # Test the wrapper
    test_code = '''
    size(100);
    draw((0,0)--(1,1));
    '''
    success = compile_asy_to_svg(test_code, "test_wrapper.svg")
    print(f"Compilation success: {success}")
    if success and os.path.exists("test_wrapper.svg"):
        print("Test SVG created.")
        os.unlink("test_wrapper.svg")
