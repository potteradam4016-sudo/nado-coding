import sys

def display_menu():
    """메뉴를 출력합니다."""
    print("\n--- 할 일 목록 관리자 ---")
    print("1. 할 일 추가 (add)")
    print("2. 할 일 보기 (view)")
    print("3. 할 일 완료 (done)")
    print("4. 할 일 삭제 (delete)")
    print("5. 종료 (exit)")
    print("-----------------------")

def add_task(tasks):
    """새로운 할 일을 목록에 추가합니다."""
    task_description = input("추가할 할 일을 입력하세요: ")
    if task_description:
        tasks.append({"task": task_description, "done": False})
        print(f"'{task_description}' 할 일이 추가되었습니다.")
    else:
        print("할 일 내용을 입력해야 합니다.")

def view_tasks(tasks):
    """현재 할 일 목록을 출력합니다."""
    if not tasks:
        print("할 일 목록이 비어 있습니다.")
        return

    print("\n--- 현재 할 일 목록 ---")
    for index, task_item in enumerate(tasks):
        status = "[x]" if task_item["done"] else "[ ]"
        print(f"{index + 1}. {status} {task_item['task']}")
    print("-----------------------")

def mark_done(tasks):
    """특정 할 일을 완료 상태로 변경합니다."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("완료할 할 일의 번호를 입력하세요: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"'{tasks[task_num - 1]['task']}' 할 일이 완료 처리되었습니다.")
        else:
            print("잘못된 번호입니다. 목록에 있는 번호를 입력해주세요.")
    except ValueError:
        print("숫자를 입력해주세요.")

def delete_task(tasks):
    """특정 할 일을 목록에서 삭제합니다."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("삭제할 할 일의 번호를 입력하세요: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task['task']}' 할 일이 삭제되었습니다.")
        else:
            print("잘못된 번호입니다. 목록에 있는 번호를 입력해주세요.")
    except ValueError:
        print("숫자를 입력해주세요.")

def main():
    """메인 함수로 프로그램의 흐름을 제어합니다."""
    tasks = [] # 할 일 목록을 저장할 리스트

    while True:
        display_menu()
        command = input("명령어를 입력하세요 (add, view, done, delete, exit): ").lower().strip()

        if command == "add":
            add_task(tasks)
        elif command == "view":
            view_tasks(tasks)
        elif command == "done":
            mark_done(tasks)
        elif command == "delete":
            delete_task(tasks)
        elif command == "exit":
            print("프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            sys.exit() # 프로그램 종료
        else:
            print("잘못된 명령어입니다. 메뉴를 다시 확인해주세요.")

if __name__ == "__main__":
    main()
