
TO_FIND_TEST="Hello World"

CHARACTERS_LIST=" !@#$%^&*()0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

import time

def find_and_print_from_characters(to_find, sleep=False):
    found=""
    for char_to_find in to_find:
        for ch in CHARACTERS_LIST:
            print(found+ch)
            if sleep:
                time.sleep(0.01)
            if char_to_find == ch:
                found+=ch
                break
    return found


def find_hello_world(sleep=False):
    return find_and_print_from_characters(TO_FIND_TEST, sleep)

def return_hello_world(sleep=False):
    return find_hello_world(sleep)



if __name__ == "__main__":
    final_response=return_hello_world(sleep=True)
    print(final_response)
