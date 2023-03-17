# -*- coding:utf-8 -*-

import tiktoken


def compare_encodings(example_string: str) -> None:
    """Prints a comparison of three string encodings."""
    # print the example string
    print(f'\nExample string: "{example_string}"')
    # for each encoding, print the # of tokens, the token integers, and the token bytes
    for encoding_name in ["gpt2", "p50k_base", "cl100k_base"]:
        encoding = tiktoken.get_encoding(encoding_name)
        token_integers = encoding.encode(example_string)
        num_tokens = len(token_integers)
        token_bytes = [encoding.decode_single_token_bytes(token) for token in token_integers]
        print()
        print(f"{encoding_name}: {num_tokens} tokens")
        print(f"token integers: {token_integers}")
        print(f"token bytes: {token_bytes}")

compare_encodings("对于业余爱好者而言，使用哪种Log格式需要根据自身拍摄需求、后期处理能力和经验等因素进行选择。以下是一些建议，帮助您选择最适合的Log格式：1. 如果您是初学者或拍摄的场景比较简单，建议选择较为通用的Log格式，如Sony的S-Log或Canon的C-Log。这些格式较为易于使用，有大量的教程和预设可供使用，可以快速得到令人满意的结果。2. 如果您已经有一定的后期处理经验，并且希望在后期进行更精细的调色和校正，建议选择支持更大动态范围和异常细节的Log格式，如Sony的S-Log2和S-Log3、Canon的C-Log2和C-Log3等。3. 如果您希望在拍摄过程中得到即时的HDR效果，并且不需要太多的后期处理，建议选择支持Hybrid Log-Gamma（HLG）格式的设备和应用程序。HLG提供HDR和SDR两种模式的兼容性，并且可以在支持HDR的电视上直接观看，极大地方便了业余爱好者的使用。总之，选择合适的Log格式需要根据个人需要和经验水平评估来决定。在使用任何Log格式之前，建议多了解一些相关的文档、指南和教程，以便更充分地理解其工作原理和使用方法。总之，选择合适的Log格式需要根据个人需要和经验水平评估来决定。在使用任何Log格式之前，建议多了解一些相关的文档、指南和教程，以便更充分地理解其工作原理和使用方法。")