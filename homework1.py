from gooey import Gooey, GooeyParser

@Gooey(program_name="even and odd numbers")
def main():
    parser = GooeyParser()
    parser.add_argument("num1", help="First number")
    parser.add_argument("num2", help="Second number")
    parser.add_argument("num3", help="Third number")
    parser.add_argument("num4", help="Fourth number")
    args = parser.parse_args()
    result = []
    numbers = int(args.num1) , int(args.num2) , int(args.num3) , int(args.num4)
    for num in range(len(numbers)):
        if numbers[num] % 2 == 0:
            result.append(f'{numbers[num]} is even')
        else:
            result.append(f'{numbers[num]} is odd')
    for i in range(len(result)):
        print(result[i])
main()