import sqlite3
import datetime
import pandas as pd


class MEMO:
    def __init__(self):
        self.conn = sqlite3.connect("memo.db")
        self.c = self.conn.cursor()

    def write(self, text: str = ""):
        """
        一言メモを記入する
        """
        d = datetime.datetime.now()
        self.c.execute("""
        INSERT INTO memo_table (date, memo) values (?, ?)        
        """, (d, text))
        self.conn.commit()
        return "記入しました。"

    def display(self):
        """
        メモの一覧を表示
        """
        self.c.execute("""
        SELECT * FROM memo_table 
        """)
        val = {"Date": [], "Memo": []}
        for id, date, memo in self.c.fetchall():
            val["Date"].append(date)
            val["Memo"].append(memo)
        return pd.DataFrame(val)

    def help_memo(self):
        """
        メソッドの説明を表示
        """
        help_comment = \
            """
        write(text: str)
            arg:text
            一言メモを記入する
        display()
            メモの一覧を表示する
        """
        print(help_comment)


def Shell(banner='', namespace={}):
    import code
    code.interact(banner=banner, local=namespace)  # namespace: dictを渡す


if __name__ == '__main__':
    var = {}  # キー(実行コマンド): メソッドの形で渡す
    m = MEMO()
    # コマンドを設定する
    var["write"] = m.write
    var["display"] = m.display
    var["help_memo"] = m.help_memo

    banner = """
　＿人人人人＿
　＞　 My Python Interactive Shell!! 　＜
　￣Y^Y^Y^Y￣
    """  # 起動時に表示される

    Shell(banner=banner, namespace=var)  # shellの起動
