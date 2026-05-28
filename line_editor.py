import flet as ft

# ArrayList 클래스
class ArrayList:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def insert(self, pos, e):
        self.items.insert(pos, e)

    def delete(self, pos):
        return self.items.pop(pos)

    def replace(self, pos, item):
        self.items[pos] = item

    def getEntry(self, pos):
        return self.items[pos]


# 라인편집기 GUI (async 방식)

async def main(page: ft.Page):
    page.title = "라인 편집기"
    page.window.width = 700
    page.window.height = 600
    page.padding = 20

    doc = ArrayList()

    # ── UI 컴포넌트 ──
    status_text = ft.Text("명령을 선택하세요.", color=ft.Colors.BLUE_600)

    line_num_field = ft.TextField(
        label="행 번호 (1부터 시작)",
        width=160,
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    content_field = ft.TextField(
        label="내용",
        width=340,
        hint_text="i, r 명령에만 사용",
    )

    doc_view = ft.Column(scroll=ft.ScrollMode.AUTO, height=260)

    # ── 문서 화면 갱신 ──
    def refresh_doc():
        doc_view.controls.clear()
        if doc.isEmpty():
            doc_view.controls.append(
                ft.Text("(문서가 비어 있습니다)", italic=True, color=ft.Colors.GREY_500)
            )
        else:
            for i in range(doc.size()):
                doc_view.controls.append(ft.Text(f"  {i + 1}.  {doc.getEntry(i)}"))
        page.update()

    # ── 다이얼로그 닫기 ──
    async def close_dialog(dlg, e):
        dlg.open = False
        page.update()

    # ── i: 라인 삽입 ──
    async def cmd_insert(_):
        num = line_num_field.value.strip()
        text = content_field.value.strip()
        if not num or not text:
            status_text.value = "⚠ 행 번호와 내용을 모두 입력하세요."
            status_text.color = ft.Colors.ORANGE_700
            page.update()
            return
        pos = int(num) - 1
        if pos < 0 or pos > doc.size():
            status_text.value = f"⚠ 행 번호는 1 ~ {doc.size() + 1} 사이여야 합니다."
            status_text.color = ft.Colors.ORANGE_700
            page.update()
            return
        doc.insert(pos, text)
        status_text.value = f"✔ {num}번 행에 삽입했습니다."
        status_text.color = ft.Colors.GREEN_700
        content_field.value = ""
        refresh_doc()

    # ── d: 라인 삭제 ──
    async def cmd_delete(_):
        num = line_num_field.value.strip()
        if not num:
            status_text.value = "⚠ 삭제할 행 번호를 입력하세요."
            status_text.color = ft.Colors.ORANGE_700
            page.update()
            return
        pos = int(num) - 1
        if pos < 0 or pos >= doc.size():
            status_text.value = f"⚠ 행 번호는 1 ~ {doc.size()} 사이여야 합니다."
            status_text.color = ft.Colors.ORANGE_700
            page.update()
            return
        removed = doc.delete(pos)
        status_text.value = f"✔ {num}번 행 삭제: '{removed}'"
        status_text.color = ft.Colors.GREEN_700
        refresh_doc()

    # ── r: 라인 변경 ──
    async def cmd_replace(_):
        num = line_num_field.value.strip()
        text = content_field.value.strip()
        if not num or not text:
            status_text.value = "⚠ 행 번호와 새 내용을 모두 입력하세요."
            status_text.color = ft.Colors.ORANGE_700
            page.update()
            return
        pos = int(num) - 1
        if pos < 0 or pos >= doc.size():
            status_text.value = f"⚠ 행 번호는 1 ~ {doc.size()} 사이여야 합니다."
            status_text.color = ft.Colors.ORANGE_700
            page.update()
            return
        doc.replace(pos, text)
        status_text.value = f"✔ {num}번 행을 변경했습니다."
        status_text.color = ft.Colors.GREEN_700
        content_field.value = ""
        refresh_doc()

    # ── l: 파일 불러오기 ──
    async def cmd_load(_):
        try:
            with open("test.txt", "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
            doc.items = lines
            status_text.value = f"✔ test.txt 로드 완료 ({len(lines)}줄)"
            status_text.color = ft.Colors.GREEN_700
        except FileNotFoundError:
            status_text.value = "⚠ test.txt 파일을 찾을 수 없습니다."
            status_text.color = ft.Colors.ORANGE_700
        refresh_doc()

    # ── s: 파일 저장 ──
    async def cmd_save(_):
        with open("test.txt", "w", encoding="utf-8") as f:
            for i in range(doc.size()):
                f.write(doc.getEntry(i) + "\n")
        status_text.value = f"✔ test.txt 저장 완료 ({doc.size()}줄)"
        status_text.color = ft.Colors.GREEN_700
        page.update()

    # ── p: 현재 내용 출력 ──
    async def cmd_print(_):
        if doc.isEmpty():
            content = ft.Text("(문서가 비어 있습니다)", italic=True, color=ft.Colors.GREY_500)
        else:
            lines = [ft.Text(f"  {i + 1}.  {doc.getEntry(i)}") for i in range(doc.size())]
            content = ft.Column(controls=lines, scroll=ft.ScrollMode.AUTO, height=300)

        async def close_print(e):
            await close_dialog(dlg, e)

        dlg = ft.AlertDialog(title=ft.Text("📄 현재 문서 내용"), content=content)
        dlg.actions = [ft.TextButton("닫기", on_click=close_print)]
        page.overlay.append(dlg)
        dlg.open = True
        status_text.value = "✔ 현재 문서 내용을 출력합니다."
        status_text.color = ft.Colors.BLUE_700
        page.update()

    # ── q: 편집기 종료 ──
    async def cmd_quit(_):
        async def do_quit(e):
            await page.window.destroy()

        dlg = ft.AlertDialog(
            title=ft.Text("편집기 종료"),
            content=ft.Text("정말 종료하시겠습니까?\n저장하지 않은 내용은 사라집니다."),
        )
        async def close_quit(e):
            await close_dialog(dlg, e)

        dlg.actions = [
            ft.TextButton("취소", on_click=close_quit),
            ft.TextButton(
                "종료",
                on_click=do_quit,
                style=ft.ButtonStyle(color=ft.Colors.RED_700),
            ),
        ]
        page.overlay.append(dlg)
        dlg.open = True
        page.update()

    # ── 버튼 행 ──
    btn_row = ft.Row(
        controls=[
            ft.ElevatedButton("i  삽입",     on_click=cmd_insert,  bgcolor=ft.Colors.BLUE_100),
            ft.ElevatedButton("d  삭제",     on_click=cmd_delete,  bgcolor=ft.Colors.RED_100),
            ft.ElevatedButton("r  변경",     on_click=cmd_replace, bgcolor=ft.Colors.ORANGE_100),
            ft.ElevatedButton("l  불러오기",  on_click=cmd_load,   bgcolor=ft.Colors.GREEN_100),
            ft.ElevatedButton("s  저장",     on_click=cmd_save,    bgcolor=ft.Colors.GREEN_100),
            ft.ElevatedButton("p  출력",     on_click=cmd_print,   bgcolor=ft.Colors.PURPLE_100),
            ft.ElevatedButton("q  종료",     on_click=cmd_quit,    bgcolor=ft.Colors.RED_200),
        ],
        wrap=True,
    )

    # ── 전체 레이아웃 ──
    page.add(
        ft.Text("라인 편집기", size=22, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Row(controls=[line_num_field, content_field]),
        ft.Container(height=8),
        btn_row,
        ft.Container(height=4),
        status_text,
        ft.Divider(),
        ft.Text("현재 문서", weight=ft.FontWeight.BOLD),
        ft.Container(
            content=doc_view,
            border=ft.border.all(1, ft.Colors.GREY_400),
            border_radius=6,
            padding=10,
            height=270,
        ),
    )

    refresh_doc()


ft.run(main)