class Calculator:
    """四則演算を行うクラス"""

    @staticmethod
    def add(a: int, b: int) -> int:
        """足し算を行う関数"""
        return a + b

if __name__ == "__main__":
    """テストコード"""
    nura = 23
    numb = 22

    print(Calculator.add(nura, numb))