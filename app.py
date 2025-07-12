import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "XXXXXXXXX"))

# To list available Gemini models, uncomment the following lines:
# if __name__ == "__main__":
#     print("Available Gemini models:")
#     for m in genai.list_models():
#         print(f"- {m.name} (methods: {getattr(m, 'supported_generation_methods', [])})")
#     exit()

# Directory containing all cloned GitHub repositories
BASE_DIR = "github_repos"
# Output file for test scenarios
OUTPUT_SPEC_FILE = "test.spec"

def generate_test_scenarios(code_snippet):
    prompt = f"Based on the following Java Spring Boot code, describe possible testing scenarios in simple English:\n\n{code_snippet}"
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    return response.text

def scan_java_files(repo_path):
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if "@RestController" in content or "@Controller" in content:
                            snippet = content[:1000]
                            scenarios = generate_test_scenarios(snippet)
                            spec_output = f"\n📄 {file} - Test Scenarios:\n{scenarios}\n"
                            with open(OUTPUT_SPEC_FILE, "a", encoding="utf-8") as spec_file:
                                spec_file.write(spec_output)
                except Exception as e:
                    error_output = f"❌ Error reading {file_path}: {e}\n"
                    with open(OUTPUT_SPEC_FILE, "a", encoding="utf-8") as spec_file:
                        spec_file.write(error_output)

def main():
    for repo_name in os.listdir(BASE_DIR):
        repo_path = os.path.join(BASE_DIR, repo_name)
        if os.path.isdir(repo_path):
            print(f"📁 Scanning local repo: {repo_name}")
            scan_java_files(repo_path)

if __name__ == "__main__":
    main()
