from gooey import Gooey, GooeyParser

@Gooey(program_name="sum of number")
def main():
    name = "moh"
    lastname = "yar"
    parser = GooeyParser()
    parser.add_argument('name', help='please enter your name')
    parser.add_argument('lastname', help='please enter your lastname')
    parser.add_argument('num1',type=float,  help='please enter number1 between 10 and 99')
    parser.add_argument('num2',type=float,  help='please enter number2 between 10 and 99')
    parser.add_argument("operation", help="please choose your operation(+, -, /, *)")
    args = parser.parse_args()
    if args.name == name and args.lastname == lastname and 10<=args.num1<=99 and 10<=args.num2<=99 :
        print("correct")
        if args.operation == "+":
            result = args.num1+args.num2
        elif args.operation == "-":
            result = args.num1-args.num2
        elif args.operation == "/":
            result = args.num1/args.num2
        elif args.operation == "*":
            result = args.num1*args.num2
        print("result is: ", result)
    else:
        print("error program")
main()