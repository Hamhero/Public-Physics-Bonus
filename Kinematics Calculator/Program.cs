using System;

class KinematicsCalculator
{
    static void Main()
    {
        Console.WriteLine("Kinematics Calculator");
        Console.WriteLine("1. Displacement");
        Console.WriteLine("2. Initial Velocity");
        Console.WriteLine("3. Final Velocity");
        Console.WriteLine("4. Acceleration");
        Console.WriteLine("5. Time");

        Console.Write("Choose what you want to calculate (1-5): ");
        int choice = int.Parse(Console.ReadLine());

        double result;

        switch (choice)
        {
            case 1:
                result = CalculateDisplacement();
                break;
            case 2:
                result = CalculateInitialVelocity();
                break;
            case 3:
                result = CalculateFinalVelocity();
                break;
            case 4:
                result = CalculateAcceleration();
                break;
            case 5:
                result = CalculateTime();
                break;
            default:
                Console.WriteLine("Invalid choice. Please choose a number between 1 and 5.");
                return;
        }

        Console.WriteLine($"Result: {result}");
    }

    static double CalculateDisplacement()
    {
        Console.Write("Enter initial velocity: ");
        double initialVelocity = double.Parse(Console.ReadLine());

        Console.Write("Enter final velocity: ");
        double finalVelocity = double.Parse(Console.ReadLine());

        Console.Write("Enter acceleration: ");
        double acceleration = double.Parse(Console.ReadLine());

        Console.Write("Enter time: ");
        double time = double.Parse(Console.ReadLine());

        return (initialVelocity + finalVelocity) * time / 2;
    }

    static double CalculateInitialVelocity()
    {
        Console.Write("Enter final velocity: ");
        double finalVelocity = double.Parse(Console.ReadLine());

        Console.Write("Enter acceleration: ");
        double acceleration = double.Parse(Console.ReadLine());

        Console.Write("Enter time: ");
        double time = double.Parse(Console.ReadLine());

        return finalVelocity - acceleration * time;
    }

    static double CalculateFinalVelocity()
    {
        Console.Write("Enter initial velocity: ");
        double initialVelocity = double.Parse(Console.ReadLine());

        Console.Write("Enter acceleration: ");
        double acceleration = double.Parse(Console.ReadLine());

        Console.Write("Enter time: ");
        double time = double.Parse(Console.ReadLine());

        return initialVelocity + acceleration * time;
    }

    static double CalculateAcceleration()
    {
        Console.Write("Enter initial velocity: ");
        double initialVelocity = double.Parse(Console.ReadLine());

        Console.Write("Enter final velocity: ");
        double finalVelocity = double.Parse(Console.ReadLine());

        Console.Write("Enter time: ");
        double time = double.Parse(Console.ReadLine());

        return (finalVelocity - initialVelocity) / time;
    }

    static double CalculateTime()
    {
        Console.Write("Enter initial velocity: ");
        double initialVelocity = double.Parse(Console.ReadLine());

        Console.Write("Enter final velocity: ");
        double finalVelocity = double.Parse(Console.ReadLine());

        Console.Write("Enter acceleration: ");
        double acceleration = double.Parse(Console.ReadLine());

        return (finalVelocity - initialVelocity) / acceleration;
    }
}
