using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Text.Json;
using System.Diagnostics;

namespace Functionality
{
    public class CalculatingItems
    {
        public void PhysicsCalculator()
        {
            System.Threading.Thread.Sleep(100);
            Console.Clear();
        }
    }
}

namespace ForDesign
{
    public class Design
    {
        public static void TypeWrite(string message, ConsoleColor color)
        {
            Console.ForegroundColor = color;
            for (int i = 0; i < message.Length; i++)
            {
                Console.Write(message[i]);
                System.Threading.Thread.Sleep(60);
            }
        }
    }
}

namespace Launching
{
    //Add paths that remain unadded
    public class Launcher
    {
        public static string grapherPath = "KinematicsGraphMaker.exe";
        public static string kinematicsCalculatorPath = "Kinematics Calculator.exe";
        public static string dynamicsCalculatorPath = "Dynamics Calculator.exe";
        public static string cannonPath = "Cannon.exe";
        public static string diagramPath = "FreeBodyDiagramMaker.exe";

        public static void Grapher()
        {
            Process.Start(grapherPath);
        }

        public static void DynamicsCalculator()
        {
            Process.Start(dynamicsCalculatorPath);
        }

        public static void KinematicsCalculator()
        {
            Process.Start(kinematicsCalculatorPath);
        }

        public static void Cannon()
        {
            Process.Start(cannonPath);
        }

        public static void FreebodyDiagram()
        {
            Process.Start(diagramPath);
        }
    }
}