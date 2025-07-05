import geometry

def main():
    print("Welcome to the Rectangle Calculator!")
    try:

        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))


        area = geometry.calculate_area(length, width)
        perimeter = geometry.calculate_perimeter(length, width)


        print(f"\nResults:")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
