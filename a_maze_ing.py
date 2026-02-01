#!/usr/bin/env python3
import sys
import os
from config_validation import read_config, validation
from maze_generator import MazeGenerator
from maze_display import MazeDisplay


def clear_screen() -> None:
    print("\033[2J\033[H", end="")
    # os.system("clear")
    print("\033[H", flush=True)


def display_menu() -> None:
    print("\n" + "\033[91m=\033[0m"*50)
    print(" "*16 + "\033[41m MAZE CONTROL MENU \033[0m")
    print("\033[91m=\033[0m"*50)
    # print("\033[92m", end="")
    print("  1. Re-generate maze")
    print("  2. Show/Hide solution path")
    print("  3. Change wall colors")
    print("  4. Change '42' pattern color")
    print("  5. Change maze generation algorithms")
    print("  6. Perfect (True or False)")
    print("  q. Quit")
    print("\033[91m=\033[0m"*50)


def get_user_choice() -> str:
    choice = input("\nEnter your choice: ").strip().lower()
    return choice


def choose_algorithm(current: str) -> str:
    """Let user choose maze generation algorithm."""
    print(f"\nCurrent algorithm: {current.upper()}")
    print("\nAvailable algorithms:")
    print("  1. Backtracking (DFS) - Long winding corridors")
    print("  2. Prim's Algorithm - Branching tree-like structure")

    choice = input("\nChoose algorithm (1-2): ").strip()

    if choice == '1':
        return 'backtracking'
    elif choice == '2':
        return 'prims'
    else:
        print("Invalid choice. Keeping current algorithm.")
        return current


def choose_perfect_mode(current: bool) -> bool:
    """Let user toggle perfect/imperfect maze mode."""
    print(f"\nCurrent mode: {'PERFECT' if current else 'IMPERFECT'}")
    print("\nChoose maze type:")
    print("  1. Perfect (only one solution path)")
    print("  2. Imperfect (multiple paths - breaks random walls)")

    choice = input("\nChoose mode (1-2): ").strip()

    if choice == '1':
        return True
    elif choice == '2':
        return False
    else:
        print("Invalid choice. Keeping current mode.")
        return current


def choose_color(current: str) -> str:
    print(f"\nCurrent color: {current.upper()}")
    print("Available colors:")
    print("  1. Red")
    print("  2. Green")
    print("  3. Yellow")
    print("  4. Blue")
    print("  5. Magenta")
    print("  6. Cyan")
    print("  7. White")

    color_map = {
        '1': 'red',
        '2': 'green',
        '3': 'yellow',
        '4': 'blue',
        '5': 'magenta',
        '6': 'cyan',
        '7': 'white'
    }

    choice = input("Choose color (1-7): ").strip()
    return color_map.get(choice, current)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)

    config_file: str = sys.argv[1]

    try:
        config = read_config(config_file)
        validation(config)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    width: int = config["WIDTH"]
    height: int = config["HEIGHT"]
    entry: tuple = config["ENTRY"]
    exit_: tuple = config["EXIT"]
    output: str = config["OUTPUT_FILE"]
    perfect: bool = config["PERFECT"]

    show_path: bool = False
    animation_speed: float = 0.02
    pattern_color: str = "yellow"
    wall_color: str = "white"
    algorithm: str = "backtracking"

    display = MazeDisplay(width, height)
    display.set_pattern_color(pattern_color)

    clear_screen()
    print("Generating maze...\n")

    maze = MazeGenerator(width, height)
    maze.add_42_pattern()
    maze.generate_backtracking(entry, display=display, delay=animation_speed)
    maze.reset_visited()

    if not perfect:
        maze.break_walls(chance=0.1)

    print("\nSolving maze...\n")
    path = maze.solve_bfs(entry, exit_, display=display, delay=animation_speed)

    maze.write_maze_hex(output, entry, exit_, path)

    clear_screen()
    print("Maze generation and solving complete!\n")
    display.display_ascii(maze.grid, entry, exit_,
                          maze.pattern_cells, path=path, show_generation=False)

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            clear_screen()
            print("Regenerating maze...\n")
            print("Watch as the maze carves through the solid blocks!\n")

            maze = MazeGenerator(width, height)
            maze.add_42_pattern()

            if algorithm == 'backtracking':
                maze.generate_backtracking(entry, display=display,
                                           delay=animation_speed)
            elif algorithm == 'prims':
                maze.generate_prims(entry, display=display,
                                    animate=True, delay=animation_speed)

            maze.reset_visited()

            if not perfect:
                maze.break_walls(chance=0.1)

            print("\nSolving maze...\n")
            path = maze.solve_bfs(entry, exit_, display=display,
                                  delay=animation_speed)
            maze.write_maze_hex(output, entry, exit_, path)

            clear_screen()
            print("Maze regenerated and solved!\n")
            display.display_ascii(maze.grid, entry, exit_, maze.pattern_cells,
                                  path if show_path else None,
                                  show_generation=False)

        elif choice == '2':
            show_path = not show_path
            clear_screen()
            if show_path:
                print("Solution path: SHOWN\n")
            else:
                print("Solution path: HIDDEN\n")
            display.display_ascii(maze.grid, entry, exit_, maze.pattern_cells,
                                  path if show_path else None,
                                  show_generation=False)

        elif choice == '3':
            print("\nChange wall color (affects all walls)")
            new_color = choose_color(wall_color)
            wall_color = new_color

            ansi_map = {
                'red': display.RED,
                'green': display.GREEN,
                'yellow': display.YELLOW,
                'blue': display.BLUE,
                'magenta': display.MAGENTA,
                'cyan': display.CYAN,
                'white': display.WHITE
            }

            display.set_color('wall', ansi_map.get(wall_color, display.WHITE))

            clear_screen()
            print(f"Wall color changed to: {wall_color.upper()}\n")
            display.display_ascii(maze.grid, entry, exit_, maze.pattern_cells,
                                  path if show_path else None,
                                  show_generation=False)

        elif choice == '4':
            print("\nChange '42' pattern color")
            new_color = choose_color(pattern_color)
            pattern_color = new_color
            display.set_pattern_color(pattern_color)

            clear_screen()
            print(f"Pattern color changed to: {pattern_color.upper()}\n")
            display.display_ascii(maze.grid, entry, exit_, maze.pattern_cells,
                                  path if show_path else None,
                                  show_generation=False)

        elif choice == '5':
            new_algorithm = choose_algorithm(algorithm)

            if new_algorithm != algorithm:
                algorithm = new_algorithm

                clear_screen()
                print(f"Regenerating maze with {algorithm.upper()}"
                      " algorithm...\n")

                maze = MazeGenerator(width, height)
                maze.add_42_pattern()

                if algorithm == 'backtracking':
                    maze.generate_backtracking(entry, display=display,
                                               delay=animation_speed)
                elif algorithm == 'prims':
                    maze.generate_prims(entry, display=display, animate=True,
                                        delay=animation_speed)

                maze.reset_visited()

                if not perfect:
                    maze.break_walls(chance=0.1)

                print("\nSolving maze...\n")
                path = maze.solve_bfs(entry, exit_, display=display,
                                      delay=animation_speed)
                maze.write_maze_hex(output, entry, exit_, path)

                clear_screen()
                print(f"Maze regenerated with {algorithm.upper()}!\n")
                display.display_ascii(maze.grid, entry, exit_,
                                      maze.pattern_cells, path=None,
                                      show_generation=False)
            else:
                clear_screen()
                print("Algorithm unchanged.\n")
                display.display_ascii(maze.grid, entry, exit_,
                                      maze.pattern_cells,
                                      path if show_path else None,
                                      show_generation=False)

        elif choice == '6':
            new_perfect = choose_perfect_mode(perfect)

            if new_perfect != perfect:
                perfect = new_perfect

                if not perfect:
                    clear_screen()
                    print("Breaking random walls to create "
                          "multiple paths...\n")
                    maze.break_walls(chance=0.1)

                    maze.reset_visited()
                    print("Re-solving maze...\n")
                    path = maze.solve_bfs(entry, exit_, display=display,
                                          delay=animation_speed)
                    maze.write_maze_hex(output, entry, exit_, path)

                    clear_screen()
                    print("Maze is now IMPERFECT (multiple paths exist)!\n")
                else:
                    clear_screen()
                    print("Regenerating maze as PERFECT...\n")

                    maze = MazeGenerator(width, height)
                    maze.add_42_pattern()

                    if algorithm == 'backtracking':
                        maze.generate_backtracking(entry, display=display,
                                                   delay=animation_speed)
                    elif algorithm == 'prims':
                        maze.generate_prims(entry, display=display,
                                            delay=animation_speed)

                    maze.reset_visited()

                    print("\nSolving maze...\n")
                    path = maze.solve_bfs(entry, exit_, display=display,
                                          delay=animation_speed)
                    maze.write_maze_hex(output, entry, exit_, path)

                    clear_screen()
                    print("Maze is now PERFECT (only one path)!\n")

                display.display_ascii(maze.grid, entry, exit_,
                                      maze.pattern_cells,
                                      path if show_path else None,
                                      show_generation=False)
            else:
                clear_screen()
                print("Mode unchanged.\n")
                display.display_ascii(maze.grid, entry, exit_,
                                      maze.pattern_cells,
                                      path if show_path else None,
                                      show_generation=False)

        elif choice == 'q':
            clear_screen()
            print("Saving final maze to file...")
            maze.write_maze_hex(output, entry, exit_, path)
            print(f"Maze saved to: {output}")
            print("\nGoodbye!")
            sys.exit(0)

        else:
            print("\nInvalid choice! Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
