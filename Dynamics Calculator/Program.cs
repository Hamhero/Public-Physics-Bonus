using System;

class DynamicsCalculator
{
    static void Main()
    {
        while (true)
        {
            Console.WriteLine("Dynamics Calculator");
            Console.WriteLine("1. Calculate Velocity");
            Console.WriteLine("2. Calculate Displacement");
            Console.WriteLine("3. Calculate Acceleration");
            Console.WriteLine("4. Calculate Time");
            Console.WriteLine("5. Calculate Force");
            Console.WriteLine("6. Calculate Mass");
            Console.WriteLine("7. Calculate Gravitational Force");
            Console.WriteLine("8. Calculate Friction Force");
            Console.WriteLine("9. Calculate Coefficient of Friction");
            Console.WriteLine("10. Calculate Normal Force");
            Console.WriteLine("11. Calculate Tension Force");
            Console.WriteLine("12. Calculate Applied Force");
            Console.WriteLine("13. Exit");

            Console.Write("Enter your choice (1-13): ");
            int choice;
            if (int.TryParse(Console.ReadLine(), out choice))
            {
                switch (choice)
                {
                    case 1:
                        CalculateVelocity();
                        break;
                    case 2:
                        CalculateDisplacement();
                        break;
                    case 3:
                        CalculateAcceleration();
                        break;
                    case 4:
                        CalculateTime();
                        break;
                    case 5:
                        CalculateForce();
                        break;
                    case 6:
                        CalculateMass();
                        break;
                    case 7:
                        CalculateGravitationalForce();
                        break;
                    case 8:
                        CalculateFrictionForce();
                        break;
                    case 9:
                        CalculateCoefficientOfFriction();
                        break;
                    case 10:
                        CalculateNormalForce();
                        break;
                    case 11:
                        CalculateTensionForce();
                        break;
                    case 12:
                        CalculateAppliedForce();
                        break;
                    case 13:
                        Environment.Exit(0);
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please enter a number between 1 and 13.");
                        break;
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid number.");
            }

            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
            Console.Clear();
        }
    }

    static void CalculateVelocity()
    {
        Console.Write("Enter initial velocity (m/s): ");
        double initialVelocity = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter acceleration (m/s^2): ");
        double acceleration = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter time (s): ");
        double time = Convert.ToDouble(Console.ReadLine());

        double velocity = initialVelocity + acceleration * time;

        Console.WriteLine($"The final velocity is: {velocity} m/s");
    }

    static void CalculateDisplacement()
    {
        Console.Write("Enter initial velocity (m/s): ");
        double initialVelocity = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter time (s): ");
        double time = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter acceleration (m/s^2): ");
        double acceleration = Convert.ToDouble(Console.ReadLine());

        double displacement = initialVelocity * time + 0.5 * acceleration * Math.Pow(time, 2);

        Console.WriteLine($"The displacement is: {displacement} meters");
    }

    static void CalculateAcceleration()
    {
        Console.Write("Enter change in velocity (m/s): ");
        double deltaVelocity = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter time (s): ");
        double time = Convert.ToDouble(Console.ReadLine());

        double acceleration = deltaVelocity / time;

        Console.WriteLine($"The acceleration is: {acceleration} m/s^2");
    }

    static void CalculateTime()
    {
        Console.Write("Enter initial velocity (m/s): ");
        double initialVelocity = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter final velocity (m/s): ");
        double finalVelocity = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter acceleration (m/s^2): ");
        double acceleration = Convert.ToDouble(Console.ReadLine());

        double time = (finalVelocity - initialVelocity) / acceleration;

        Console.WriteLine($"The time is: {time} seconds");
    }

    static void CalculateForce()
    {
        Console.Write("Enter mass (kg): ");
        double mass = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter acceleration (m/s^2): ");
        double acceleration = Convert.ToDouble(Console.ReadLine());

        double force = mass * acceleration;

        Console.WriteLine($"The force is: {force} Newtons");
    }

    static void CalculateMass()
    {
        Console.Write("Enter force (Newtons): ");
        double force = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter acceleration (m/s^2): ");
        double acceleration = Convert.ToDouble(Console.ReadLine());

        double mass = force / acceleration;

        Console.WriteLine($"The mass is: {mass} kilograms");
    }

    static void CalculateGravitationalForce()
    {
        const double G = 6.67430e-11; // Gravitational constant (m^3 kg^-1 s^-2)

        Console.Write("Enter mass of object 1 (kg): ");
        double mass1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter mass of object 2 (kg): ");
        double mass2 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter distance between the centers of the masses (m): ");
        double distance = Convert.ToDouble(Console.ReadLine());

        double gravitationalForce = G * (mass1 * mass2) / Math.Pow(distance, 2);

        Console.WriteLine($"The gravitational force is: {gravitationalForce} Newtons");
    }

    static void CalculateFrictionForce()
    {
        Console.Write("Enter coefficient of friction: ");
        double mu = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter normal force (N): ");
        double normalForce = Convert.ToDouble(Console.ReadLine());

        double frictionForce = mu * normalForce;

        Console.WriteLine($"The friction force is: {frictionForce} Newtons");
    }

    static void CalculateCoefficientOfFriction()
    {
        Console.Write("Enter friction force (N): ");
        double frictionForce = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter normal force (N): ");
        double normalForce = Convert.ToDouble(Console.ReadLine());

        double coefficientOfFriction = frictionForce / normalForce;

        Console.WriteLine($"The coefficient of friction is: {coefficientOfFriction}");
    }

    static void CalculateNormalForce()
    {
        Console.Write("Enter mass (kg): ");
        double mass = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter gravitational acceleration (m/s^2): ");
        double gravity = Convert.ToDouble(Console.ReadLine());

        double normalForce = mass * gravity;

        Console.WriteLine($"The normal force is: {normalForce} Newtons");
    }

    static void CalculateTensionForce()
    {
        Console.Write("Enter mass (kg): ");
        double mass = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter acceleration (m/s^2): ");
        double acceleration = Convert.ToDouble(Console.ReadLine());

        double tensionForce = mass * acceleration;

        Console.WriteLine($"The tension force is: {tensionForce} Newtons");
    }

    static void CalculateAppliedForce()
    {
        Console.Write("Enter mass (kg): ");
        double mass = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter acceleration (m/s^2): ");
        double acceleration = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter friction force (N): ");
        double frictionForce = Convert.ToDouble(Console.ReadLine());

        double appliedForce = mass * acceleration + frictionForce;

        Console.WriteLine($"The applied force is: {appliedForce} Newtons");
    }
}
