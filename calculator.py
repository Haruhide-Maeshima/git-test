class Calculator:
    """四則演算を行うクラス"""

    @staticmethod
    def add(a: int, b: int) -> int:
        """足し算を行う関数"""
        return a + b
    
    @staticmethod
    def sub(a: int, b: int) -> int:
        """引き算を行う関数"""
        return a - b
    
    @staticmethod
    def mul(a: int, b: int) -> int:
        """掛け算を行う関数"""
        return a * b

if __name__ == "__main__":
    """テストコード"""
    numa = 23
    numb = 22

    print(Calculator.add(numa, numb))
    print(Calculator.sub(numa, numb))
    print(Calculator.mul(numa, numb))