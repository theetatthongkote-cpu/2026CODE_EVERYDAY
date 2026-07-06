# day 174
# today i took the hsk 2 exam
# hopefully i passed lol
from typing import Union
from deep_translator import GoogleTranslator


def trans_zh_en(text: str) -> str | None:
    if not text.strip():
        return ""

    try:
        return GoogleTranslator(source="zh-CN", target="en").translate(text)
    except Exception as error:
        print(f"Log: Translation failed due to: {error}")
        return None


if __name__ == "__main__":
    sample_text = "这是一个测试。"

    # Using modern assignment expressions (Walrus Operator :=) available in Python 3.8+
    if (result := trans_zh_en(sample_text)) is not None:
        print(f"Success: {result}")
    else:
        print("Failure: Could not retrieve translation.")
