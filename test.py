from gen_code import generate_code


if __name__ == '__main__':
    languages = ['python', 'android', 'flutter', 'ios']

    for language in languages:
        code = generate_code('assistant id', 'api key', ['q1', 'q2', 'q3'],
                             ['c1', 'c2', 'c3', 'c4'], language)
        print(f'======================{language}======================')
        print(code)
        print()