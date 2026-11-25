"""
Data processing utilities for textbook examples
"""

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: A list of integers or floats
        
    Returns:
        The average value
    """
    total = 0
    for num in numbers:
        total = total + num
    return total / len(numbers)  # BUG: Does not handle empty list


def remove_duplicates(items):
    """
    Remove duplicate items from a list while preserving order.
    
    Args:
        items: A list that may contain duplicates
        
    Returns:
        A new list with duplicates removed
    """
    seen = []
    result = []
    for item in items:
        if item not in seen:  # INEFFICIENT: Should use a set for O(1) lookup
            result.append(item)
            seen.append(item)
    return result


def sort_and_filter(data, min_value=0):
    """
    Sort data and filter out values below min_value.
    
    Args:
        data: List of values to process
        min_value: Minimum value to keep (default: 0)
        
    Returns:
        Sorted, filtered list
    """
    filtered = [x for x in data if x >= min_value]
    filtered.sort()  # BUG: Does not handle None values which will cause TypeError
    return filtered


def find_max(numbers):
    """Find the maximum value in a list."""
    # BUG: Does not handle empty list or None values
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


if __name__ == "__main__":
    # Test the functions
    test_numbers = [1, 5, 3, 2, 8]
    print(f"Average: {calculate_average(test_numbers)}")  # OK
    
    test_items = ["a", "b", "a", "c", "b"]
    print(f"Unique: {remove_duplicates(test_items)}")  # OK but inefficient
    
    # This will fail with None values
    mixed_data = [5, 2, None, 8, 1]
    print(f"Sorted: {sort_and_filter(mixed_data)}")
