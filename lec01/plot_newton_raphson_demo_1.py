import argparse
from math import cos, sin
from pathlib import Path

from plot_newton_raphson import plot_newton_raphson_iteration


def f(x):
    return x**3 - sin(x)


def df(x):
    return 3 * x**2 - cos(x)


parser = argparse.ArgumentParser(description="Plot the A1 Newton-Raphson demo.")
parser.add_argument("--no-show", action="store_true",
                    help="Save the figures without opening plot windows.")
args = parser.parse_args()
output_dir = Path(__file__).resolve().parent

for tol, name in ((5e-2, "low_accuracy"), (1e-8, "high_accuracy")):
    xs = plot_newton_raphson_iteration(
        f, df, x0=1.0, tol=tol,
        title=rf"$x^3-\sin x=0$, $x_0=1$, tol={tol:g}",
        save_prefix=output_dir / f"newton_raphson_demo_1_{name}",
        show=not args.no_show,
    )
    print(f"tol={tol:.0e}, root={xs[-1]:.12f}, "
          f"iterations={len(xs) - 1}, residual={abs(f(xs[-1])):.3e}")
