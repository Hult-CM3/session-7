import time
import random
from sort import SortingAlgorithms

def measure_sort_time(sort_func, arr):
    """Measure the time taken by a sorting algorithm to sort an array."""
    arr_copy = arr.copy()  # Create a copy to avoid modifying original array
    start_time = time.time()
    sorted_arr = sort_func(arr_copy)
    end_time = time.time()
    return end_time - start_time, sorted_arr

def compare_sorting_algorithms(arr_size=1000):
    """Compare the performance of different sorting algorithms."""
    # Create test arrays
    random_array = [random.randint(1, 1000) for _ in range(arr_size)]
    sorted_array = list(range(arr_size))
    reverse_array = list(range(arr_size, 0, -1))
    
    # Test cases to try
    test_arrays = {
        "Random": random_array,
        "Already Sorted": sorted_array,
        "Reverse Sorted": reverse_array
    }
    
    # Dictionary to store all sorting functions
    sorting_functions = {
        "Sort 1": SortingAlgorithms().sort_one,
        "Sort 2": SortingAlgorithms().sort_two,
        "Sort 3": SortingAlgorithms().sort_three,
    }
    
    # Compare each sorting algorithm with each test case
    results = {}
    for array_type, test_arr in test_arrays.items():
        print(f"\nTesting with {array_type} array:")
        print("-" * 40)
        
        for sort_name, sort_func in sorting_functions.items():
            time_taken, _ = measure_sort_time(sort_func, test_arr)
            print(f"{sort_name}: {time_taken:.4f} seconds")
            
            # Store results for later analysis
            if array_type not in results:
                results[array_type] = {}
            results[array_type][sort_name] = time_taken
            
    return results

if __name__ == "__main__":
    # Run comparison with different array sizes
    print("Testing with small array (100 elements)")
    results_small = compare_sorting_algorithms(100)
    
    print("\nTesting with medium array (1000 elements)")
    results_medium = compare_sorting_algorithms(1000)
    
    print("\nTesting with large array (5000 elements)")
    results_large = compare_sorting_algorithms(5000)
