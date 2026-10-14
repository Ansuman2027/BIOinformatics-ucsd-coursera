def pattern_count(text: str, pattern: str) -> int:
    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if text[i:i + k] == pattern:
            count += 1
    return count


if __name__ == "__main__":
    
    test_text = "GCGCG"
    test_pattern = "GCG"
    print(f"Pattern '{test_pattern}' appears in '{test_text}': {pattern_count(test_text, test_pattern)} times")
