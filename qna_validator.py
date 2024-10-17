from pathlib import Path

def has_answer_in_question(questions):
    for question in questions:
        if 'ལན' in question:
            return True
    return False

def is_valid_qna_book(book_id):
    questions = Path(f'./data/Questions/{book_id}.txt').read_text(encoding='utf-8').split('\n')
    answers = Path(f'./data/Answers/{book_id}.txt').read_text(encoding='utf-8').split('\n')
    if len(questions) != len(answers):
        return False
    if has_answer_in_question(questions):
        return False
    return True

if __name__ == "__main__":
    book_paths = list(Path('./data/Questions').iterdir())
    book_paths.sort()
    invalid_book_ids = []
    for book_path in book_paths:
        book_id = book_path.stem
        if not is_valid_qna_book(book_id):
            invalid_book_ids.append(book_id)
            print(f"Book {book_id} is invalid")
        # else:
        #     print(f"Book {book_id} is valid")