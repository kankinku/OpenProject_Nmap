import os

def find_files_with_keyword_in_content(root_dir, keyword):
    """
    하위 폴더를 포함하여 파일 내용에 특정 단어가 포함된 파일을 검색합니다.

    :param root_dir: 검색을 시작할 루트 디렉토리 경로
    :param keyword: 검색할 키워드
    :return: 검색된 파일 경로의 리스트
    """
    matching_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    if keyword in file.read():
                        matching_files.append(file_path)
            except (UnicodeDecodeError, PermissionError, FileNotFoundError):
                # 파일을 읽을 수 없는 경우 예외 처리
                pass
    return matching_files

# 사용 예시
if __name__ == "__main__":
    search_directory = input("검색할 디렉토리 경로를 입력하세요: ")
    search_keyword = input("검색할 키워드를 입력하세요: ")

    result_files = find_files_with_keyword_in_content(search_directory, search_keyword)
    
    if result_files:
        print(f"'{search_keyword}'를 포함하는 파일들:")
        for file in result_files:
            print(file)
    else:
        print(f"'{search_keyword}'를 포함하는 파일을 찾을 수 없습니다.")
