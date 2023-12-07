using System;
using Functionality;
using ForDesign;
using Launching;

namespace Main
{
    class PhysicsProject
    {
        public static CalculatingItems calculating = new CalculatingItems();
        public static Launcher launcher = new Launcher();

        static string choice;

        static void Main(string[] args)
        {

            while(true)
            {
                Console.Clear();
                Design.TypeWrite($"Welcome to my program! What would you like to launch?\nA. Launch Physics Grapher\nB. Kinematics Calculator\nC. Dynamics Calculator\nD. Free Body Diagram Maker\nE. Cannon Simulator\nF. Exit\n\n", ConsoleColor.White);
                choice = Console.ReadLine();

                if (choice.ToLower() == "a")
                {
                    Console.Clear();
                    Design.TypeWrite("The Physics Grapher has been launched!\n\n", ConsoleColor.Red);
                    Launcher.Grapher();
                    System.Threading.Thread.Sleep(1000);
                }

                else if (choice.ToLower() == "b")
                {
                    Console.Clear();
                    Design.TypeWrite("The Kinematics Calculator has been launched!\n\n", ConsoleColor.Red);
                    Launcher.KinematicsCalculator();
                    System.Threading.Thread.Sleep(1000);
                }

                else if (choice.ToLower() == "c")
                {
                    Console.Clear();
                    Design.TypeWrite("The Dynamics Calculator has been launched!\n\n", ConsoleColor.Red);
                    Launcher.DynamicsCalculator();
                    System.Threading.Thread.Sleep(1000);
                }

                else if(choice.ToLower() == "d")
                {
                    Console.Clear();
                    Design.TypeWrite("The Freebody diagram maker has been launched!\n\n", ConsoleColor.Red);
                    Launcher.FreebodyDiagram();
                    System.Threading.Thread.Sleep(1000);
                }

                else if(choice.ToLower() == "e")
                {
                    Console.Clear();
                    Design.TypeWrite("The Cannon Simulator has been launched!\n\n", ConsoleColor.Red);
                    Launcher.Cannon();
                    System.Threading.Thread.Sleep(1000);
                }

                else if (choice.ToLower() == "f")
                {
                    Console.Clear();
                    Design.TypeWrite("Program Exited", ConsoleColor.Red);
                    System.Threading.Thread.Sleep(1000);
                    break;
                }

                else
                {
                    Console.Clear();
                    Design.TypeWrite("That is an unacceptable answer!\n\n", ConsoleColor.Yellow);
                }
            }
        }
    }
}
