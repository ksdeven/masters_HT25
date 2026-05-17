"""
MASTER GUIDE — single integrated document
Merges: BSpline_Physics_Guide + BSpline_Repo_Complete_Guide
Logical order:
  Cover → TOC → Roadmap → Python/NumPy/SciPy/matplotlib basics
  → B-spline theory → THE LIBRARY (full anatomy)
  → Assignments 4 / 5 / 6 (each: physics → library calls → complete code)
  → Debugging checklist → Quick-reference sheet
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Preformatted, HRFlowable, Table, TableStyle, KeepTogether
)
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT

W, H = A4

# ── palette ───────────────────────────────────────────────────────
DARK    = colors.HexColor("#1a237e")
MID     = colors.HexColor("#3949ab")
LITE    = colors.HexColor("#e8eaf6")
CODEBG  = colors.HexColor("#f5f5f5")
GREENBG = colors.HexColor("#e8f5e9")
ORANGEBG= colors.HexColor("#fff3e0")
YELLBG  = colors.HexColor("#fffde7")
REDBG   = colors.HexColor("#ffebee")
LIBHDR  = colors.HexColor("#4a148c")   # purple — library sections
LIBLT   = colors.HexColor("#f3e5f5")

base = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, parent=base["Normal"], **kw)

# ── text styles ───────────────────────────────────────────────────
H1   = S("H1",  fontSize=19, textColor=DARK,   spaceBefore=20, spaceAfter=6,
         fontName="Helvetica-Bold")
H2   = S("H2",  fontSize=13, textColor=MID,    spaceBefore=13, spaceAfter=4,
         fontName="Helvetica-Bold")
H3   = S("H3",  fontSize=10.5,textColor=DARK,  spaceBefore=9,  spaceAfter=3,
         fontName="Helvetica-Bold")
H2LIB= S("H2L", fontSize=13, textColor=LIBHDR, spaceBefore=13, spaceAfter=4,
         fontName="Helvetica-Bold")
BODY = S("BD",  fontSize=9.5, leading=15, spaceAfter=5, alignment=TA_JUSTIFY)
BUL  = S("BUL", fontSize=9.5, leading=14, spaceAfter=3,
         leftIndent=14, firstLineIndent=-10)
CODE = S("CD",  fontSize=7.9, leading=11.5, fontName="Courier",
         backColor=CODEBG, leftIndent=8, rightIndent=8,
         spaceBefore=4, spaceAfter=6, borderPad=5)
NOTE = S("NT",  fontSize=9, leading=13, backColor=GREENBG,
         leftIndent=8, rightIndent=8, spaceBefore=3, spaceAfter=5,
         borderPad=6, fontName="Helvetica-Oblique")
WARN = S("WN",  fontSize=9, leading=13, backColor=ORANGEBG,
         leftIndent=8, rightIndent=8, spaceBefore=3, spaceAfter=5,
         borderPad=6, fontName="Helvetica-Oblique")
TIP  = S("TP",  fontSize=9, leading=13, backColor=LITE,
         leftIndent=8, rightIndent=8, spaceBefore=3, spaceAfter=5,
         borderPad=6, fontName="Helvetica-Oblique")
KEY  = S("KY",  fontSize=9, leading=13, backColor=YELLBG,
         leftIndent=8, rightIndent=8, spaceBefore=3, spaceAfter=5,
         borderPad=6, fontName="Helvetica-Bold")
LIBBOX=S("LB",  fontSize=9, leading=13, backColor=LIBLT,
         leftIndent=8, rightIndent=8, spaceBefore=3, spaceAfter=5,
         borderPad=6, fontName="Helvetica-Oblique", textColor=LIBHDR)
TITL = S("TT",  fontSize=26, textColor=DARK, fontName="Helvetica-Bold",
         alignment=TA_CENTER, spaceBefore=50, spaceAfter=8)
SUBT = S("ST",  fontSize=12, textColor=MID,  fontName="Helvetica-Oblique",
         alignment=TA_CENTER, spaceAfter=5)
SECBAR=S("SB",  fontSize=9.5, textColor=colors.white, fontName="Helvetica-Bold",
         backColor=MID, leftIndent=6, borderPad=5,
         spaceAfter=2, spaceBefore=9)
LIBBAR=S("LBB", fontSize=9.5, textColor=colors.white, fontName="Helvetica-Bold",
         backColor=LIBHDR, leftIndent=6, borderPad=5,
         spaceAfter=2, spaceBefore=9)

def code(t):    return Preformatted(t.strip("\n"), CODE)
def h1(t):      return Paragraph(t, H1)
def h2(t):      return Paragraph(t, H2)
def h2lib(t):   return Paragraph(t, H2LIB)
def h3(t):      return Paragraph(t, H3)
def p(t):       return Paragraph(t, BODY)
def note(t):    return Paragraph("&#x2705;  " + t, NOTE)
def warn(t):    return Paragraph("&#x26A0;  " + t, WARN)
def tip(t):     return Paragraph("&#x1F4A1; " + t, TIP)
def key(t):     return Paragraph("&#x1F511; KEY: " + t, KEY)
def libbox(t):  return Paragraph("&#x1F4E6; LIBRARY: " + t, LIBBOX)
def b(t):       return Paragraph("&#x2022;  " + t, BUL)
def sp(n=6):    return Spacer(1, n)
def hr():       return HRFlowable(width="100%", thickness=0.5, color=MID,
                                  spaceAfter=4, spaceBefore=4)
def hrlib():    return HRFlowable(width="100%", thickness=0.5, color=LIBHDR,
                                  spaceAfter=4, spaceBefore=4)
def secbar(t):  return Paragraph("  " + t, SECBAR)
def libbar(t):  return Paragraph("  " + t, LIBBAR)

def tbl(rows, col_widths, header_bg=DARK):
    t = Table(rows, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,0), header_bg),
        ("TEXTCOLOR",    (0,0), (-1,0), colors.white),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 8.5),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LITE]),
        ("GRID",         (0,0), (-1,-1), 0.4, colors.grey),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
    ]))
    return t

story = []

# ════════════════════════════════════════════════════════════════════
# COVER
# ════════════════════════════════════════════════════════════════════
story += [
    sp(35),
    Paragraph("B-Splines &amp; Atomic Physics", TITL),
    Paragraph("Complete Self-Study Guide — Assignments 4, 5 &amp; 6", SUBT),
    Paragraph("Python · NumPy · SciPy · johntfoster/bspline · Poisson · Hydrogen · DFT", SUBT),
    sp(18), hr(), sp(10),
    Paragraph(
        "A single integrated reference covering everything from Python basics "
        "to a working self-consistent-field DFT code. "
        "Includes a full anatomy of the <b>johntfoster/bspline</b> library — "
        "every class, method, and utility function explained and mapped "
        "to the exact line of code where you call it.",
        S("cv", fontSize=10.5, alignment=TA_CENTER,
          fontName="Helvetica-Oblique", textColor=colors.grey)
    ),
    sp(16),
    Paragraph(
        "Colour key:  "
        "<font color='#3949ab'><b>Blue headers</b></font> = physics / maths content    "
        "<font color='#4a148c'><b>Purple headers</b></font> = johntfoster/bspline library",
        S("ck", fontSize=9, alignment=TA_CENTER,
          fontName="Helvetica-Oblique", textColor=colors.grey)
    ),
    PageBreak(),
]

# ════════════════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ════════════════════════════════════════════════════════════════════
story += [
    h1("Contents"),
    p("<b>PART A — FOUNDATIONS</b>"),
    p("1.  Weekend Roadmap &amp; Time Plan"),
    p("2.  Python Crash Course — Variables, Lists, Loops, Indexing"),
    p("3.  NumPy Essentials — Arrays, Matrix Operations, Boolean Indexing"),
    p("4.  SciPy — Linear Solvers and Eigenvalue Problems"),
    p("5.  matplotlib — Plotting Results"),
    sp(4),
    p("<b>PART B — B-SPLINES</b>"),
    p("6.  B-Spline Theory from First Principles"),
    p("7.  The johntfoster/bspline Library — Repository Layout"),
    p("8.  The Order Convention: Library p vs Assignment k  (READ THIS)"),
    p("9.  bspline.py — Class Bspline: Every Method Explained"),
    p("    9.1  augknt()  —  Building the knot vector  [first call you make]"),
    p("    9.2  Bspline(t, p)  —  Creating the basis object"),
    p("    9.3  B(x)  —  All basis function values at a point"),
    p("    9.4  B.d(x)  —  First derivatives (fast path)"),
    p("    9.5  B.diff(order)  —  Any-order derivative as a callable"),
    p("    9.6  B.collmat(tau, deriv_order)  —  The collocation matrix  [KEY]"),
    p("    9.7  splinelab utilities: aptknt, aveknt, knt2mlt, spcol"),
    p("    9.8  The memoize cache — why you create Bspline once"),
    sp(4),
    p("<b>PART C — ASSIGNMENTS</b>"),
    p("10. Assignment 4 — Poisson Collocation"),
    p("    10.1  Physics and equation"),
    p("    10.2  Method step by step"),
    p("    10.3  Library calls mapped to each step"),
    p("    10.4  Complete working code"),
    p("    10.5  Analytical solutions for checking"),
    p("11. Assignment 5 — Hydrogen Eigenvalue Problem"),
    p("    11.1  Physics and Galerkin formulation"),
    p("    11.2  Library calls for matrix construction"),
    p("    11.3  Complete working code"),
    p("    11.4  Exponential knot sequence"),
    p("12. Assignment 6 — Self-Consistent Field for Many-Electron Atoms"),
    p("    12.1  The SCF loop"),
    p("    12.2  Aufbau filling"),
    p("    12.3  Charge density, exchange, convergence"),
    p("    12.4  Complete SCF skeleton"),
    sp(4),
    p("<b>PART D — REFERENCE</b>"),
    p("13. Debugging Checklist"),
    p("14. What the Library Does NOT Do"),
    p("15. Quick-Reference Formula Sheet"),
    PageBreak(),
]

# ════════════════════════════════════════════════════════════════════
# PART A — FOUNDATIONS
# ════════════════════════════════════════════════════════════════════
story += [Paragraph("PART A — FOUNDATIONS", S("PA", fontSize=16,
          textColor=colors.white, backColor=DARK, fontName="Helvetica-Bold",
          alignment=TA_CENTER, spaceBefore=6, spaceAfter=6, borderPad=8)),
    PageBreak()]

# ── Section 1: Roadmap ───────────────────────────────────────────
story += [
    h1("1. Weekend Roadmap &amp; Time Plan"),
    p("You have roughly <b>two full days</b> plus a polishing day. "
      "The table below is a realistic schedule assuming you follow this guide linearly."),
    sp(5),
]
story += [tbl([
    ["Time block", "Goal", "Sections here"],
    ["Sat morning (3 h)",  "Python + NumPy + B-spline theory\nWrite knot vector, plot all splines", "2, 3, 6, 7–9"],
    ["Sat afternoon (4 h)","Assignment 4 — Poisson collocation\nTest uniform sphere against analytical", "4, 10"],
    ["Sat evening (2 h)",  "Assignment 4 — shell + hydrogen cases\nLU reuse, plots", "10"],
    ["Sun morning (4 h)",  "Assignment 5 — hydrogen eigenvalue\nBuild H and S via Gauss quadrature", "4, 11"],
    ["Sun afternoon (3 h)","Assignment 5 — multiple ℓ values, wave functions\nAssignment 6 — SCF skeleton", "11, 12"],
    ["Sun evening (3 h)",  "Assignment 6 — helium convergence\nNeon orbital energies", "12"],
    ["Monday (4 h)",       "Polish code · make plots · build presentation", "13, 14, 15"],
], [3.2*cm, 7.5*cm, 4.5*cm]), sp(8),
    note("Assignments 4 and 5 share 90 % of the same B-spline code. "
         "Build the knot vector and Bspline object once in a shared file; "
         "import it in both assignments."),
    PageBreak()]

# ── Section 2: Python crash course ──────────────────────────────
story += [
    h1("2. Python Crash Course — the Pieces You Actually Need"),
    h2("2.1 Variables and Types"),
    p("Python variables hold references to objects. "
      "You will use four types almost exclusively: <b>float</b>, <b>int</b>, "
      "<b>numpy array</b>, and <b>dict</b> (for storing named results)."),
    code("""
x    = 3.14          # float
n    = 10            # integer
flag = True          # boolean
name = "hydrogen"    # string (rarely needed in physics code)

# Dictionary — useful for storing orbital results keyed by (n, ell)
energies = {}
energies[(1, 0)] = -0.5      # store ground-state energy
print(energies[(1, 0)])      # -0.5
"""),
    h2("2.2 Lists vs NumPy Arrays — Use Arrays for All Numerics"),
    code("""
py_list = [1, 2, 3]               # Python list — no fast maths
import numpy as np
arr = np.array([1.0, 2.0, 3.0])   # NumPy array — vectorised maths

arr * 2          # array([2., 4., 6.])   — no loop needed
arr ** 2         # array([1., 4., 9.])
np.sqrt(arr)     # array([1., 1.41, 1.73])
np.sum(arr)      # 6.0
"""),
    h2("2.3 Loops and range()"),
    code("""
for i in range(5):       # i = 0, 1, 2, 3, 4
    print(i)

for i in range(1, 10, 2):   # 1, 3, 5, 7, 9
    print(i)

# Enumerate gives index + value simultaneously
r_vals = np.linspace(0, 10, 5)
for idx, r in enumerate(r_vals):
    print(idx, r)           # 0 0.0 / 1 2.5 / ...
"""),
    h2("2.4 Zero-Based Indexing"),
    code("""
a = np.array([10., 20., 30., 40., 50.])
a[0]       # 10.0  — first element
a[-1]      # 50.0  — last element
a[1:4]     # [20., 30., 40.]  — slice, end is exclusive
a[::2]     # [10., 30., 50.]  — every second element
"""),
    PageBreak(),
]

# ── Section 3: NumPy ─────────────────────────────────────────────
story += [
    h1("3. NumPy Essentials"),
    h2("3.1 Creating Arrays"),
    code("""
import numpy as np
np.zeros(10)               # [0. 0. 0. ...]  length 10
np.zeros((5, 5))           # 5×5 matrix of zeros
np.linspace(0, 10, 50)    # 50 evenly spaced points from 0 to 10
np.eye(5)                  # 5×5 identity matrix
np.unique(t)               # sorted unique values — used for knot points
"""),
    h2("3.2 Matrix Operations — Core of All Three Assignments"),
    code("""
A = np.zeros((4, 4))
A[0, 0] = 1.0              # set element
A[2, :] = np.array([1,2,3,4])   # fill entire row
A[:, 3] = np.array([0,1,2,3])   # fill entire column

b = np.array([1., 2., 3., 4.])

x = np.linalg.solve(A, b)  # solve A x = b
y = A @ b                   # matrix-vector multiply  (same as np.dot(A, b))

# Matrix-matrix multiply: used with collmat results
A_plot = B.collmat(r_values)   # shape (N_r, n_basis)
phi    = A_plot @ c            # shape (N_r,)  — reconstructed function
"""),
    h2("3.3 Boolean Indexing — for Charge Densities"),
    code("""
r   = np.linspace(0, 15, 200)
R   = 5.0
rho = np.zeros_like(r)
rho[r <= R] = 3.0 / (4 * np.pi * R**3)   # uniform inside sphere
# rho[r > R] is already 0.0
"""),
    h2("3.4 Integration with trapz"),
    code("""
# Quick check: does 4*pi * int rho r^2 dr = Q ?
check = 4 * np.pi * np.trapz(rho * r**2, r)
print(f"Charge = {check:.4f}")   # should equal Q = 1.0
"""),
    PageBreak(),
]

# ── Section 4: SciPy ─────────────────────────────────────────────
story += [
    h1("4. SciPy — Linear Solvers and Eigenvalue Problems"),
    h2("4.1 LU Factorisation — Solve Once, Reuse Many Times  (Assignment 4)"),
    p("Poisson's equation gives the same matrix A for all three charge distributions. "
      "LU-factorising once and calling lu_solve three times saves 2/3 of the work."),
    code("""
from scipy.linalg import lu_factor, lu_solve

lu, piv = lu_factor(A)          # factorise ONCE — O(N^3)
c_sphere = lu_solve((lu, piv), rhs_sphere)   # O(N^2) each
c_shell  = lu_solve((lu, piv), rhs_shell)
c_hydro  = lu_solve((lu, piv), rhs_hydro)
"""),
    h2("4.2 Generalised Eigenvalue Problem  (Assignment 5 &amp; 6)"),
    p("The Galerkin formulation gives  <b>H c = E S c</b>  where both H and S are "
      "symmetric. Use <b>eigh</b> (not eig) — it exploits symmetry and returns "
      "real eigenvalues in sorted order."),
    code("""
from scipy.linalg import eigh

eigenvalues, eigenvectors = eigh(H_mat, S_mat)
# eigenvalues[i]     — i-th energy (Hartree), sorted ascending
# eigenvectors[:,i]  — corresponding coefficient vector c_i

# Bound states have negative energy:
bound = eigenvalues[eigenvalues < 0]
print(f"Found {len(bound)} bound states")
print(f"Ground state: {bound[0]:.6f} Ha  (exact for H: -0.5 Ha)")
"""),
    h2("4.3 Gauss-Legendre Quadrature — Exact Integration of B-Spline Products"),
    p("B-splines are piecewise polynomials of degree p. "
      "Products of two basis functions are polynomials of degree 2p. "
      "Gauss-Legendre with <b>p+1</b> points per interval integrates these exactly."),
    code("""
from numpy.polynomial.legendre import leggauss

ngl = 5                              # points per interval (p+1 = 4 is minimum)
gl_z, gl_w = leggauss(ngl)           # nodes and weights on [-1, 1]

# Transform to interval [a, b]:
def gl_on(a, b):
    x = 0.5*(b-a)*gl_z + 0.5*(b+a)  # points in [a, b]
    w = 0.5*(b-a)*gl_w               # scaled weights
    return x, w

# Test: integrate r^2 from 0 to 5
x, w = gl_on(0, 5)
print(np.sum(w * x**2))   # should be 5^3/3 = 41.667
"""),
    PageBreak(),
]

# ── Section 5: matplotlib ────────────────────────────────────────
story += [
    h1("5. matplotlib — Plotting Results"),
    code("""
import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.01, 10, 300)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(r, -1.0/r,  "b-",  linewidth=1.5, label="V = -1/r  (Coulomb)")
ax.plot(r, np.exp(-2*r), "r--", label="rho ~ exp(-2r)  (H 1s)")
ax.set_xlabel("r  [Bohr]")
ax.set_ylabel("value")
ax.set_xlim(0, 10);  ax.set_ylim(-3, 1.1)
ax.legend();  ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("result.png", dpi=150)   # save for report
plt.show()

# Multiple subplots — useful for comparing assignments
fig, axes = plt.subplots(1, 3, figsize=(13, 4))
axes[0].set_title("Sphere")
axes[1].set_title("Shell")
axes[2].set_title("Hydrogen 1s")
"""),
    PageBreak(),
]

# ════════════════════════════════════════════════════════════════════
# PART B — B-SPLINES
# ════════════════════════════════════════════════════════════════════
story += [Paragraph("PART B — B-SPLINES", S("PB", fontSize=16,
          textColor=colors.white, backColor=DARK, fontName="Helvetica-Bold",
          alignment=TA_CENTER, spaceBefore=6, spaceAfter=6, borderPad=8)),
    PageBreak()]

# ── Section 6: Theory ────────────────────────────────────────────
story += [
    h1("6. B-Spline Theory from First Principles"),
    h2("6.1 What is a Knot Sequence?"),
    p("A knot sequence is a non-decreasing list  t[0] &#x2264; t[1] &#x2264; ... &#x2264; t[N-1]. "
      "Think of it as the grid skeleton on which your basis functions live. "
      "Repeated values at the boundaries force the splines to be exactly zero there."),
    code("""
# Manual construction (assignment PDF convention, k=4):
k     = 4                           # order in assignment notation
r_max = 20.0
inner = np.linspace(0, r_max, 12)  # 12 distinct physical points
t = np.concatenate([
    np.repeat(inner[0],   k),       # k=4 copies of 0
    inner[1:-1],                    # 10 interior points
    np.repeat(inner[-1],  k)        # k=4 copies of r_max
])
# len(t) = 4 + 10 + 4 = 18
# n_splines = len(t) - k = 18 - 4 = 14
"""),
    h2("6.2 The Recursive Definition (Cox–de Boor)"),
    p("<b>Order 1:</b>  B<sub>i,1</sub>(x) = 1 if t<sub>i</sub> &#x2264; x &lt; t<sub>i+1</sub>, else 0"),
    p("<b>Order k:</b>  B<sub>i,k</sub>(x) = "
      "[(x&#x2212;t<sub>i</sub>)/(t<sub>i+k&#x2212;1</sub>&#x2212;t<sub>i</sub>)] B<sub>i,k&#x2212;1</sub>(x)  "
      "+ [(t<sub>i+k</sub>&#x2212;x)/(t<sub>i+k</sub>&#x2212;t<sub>i+1</sub>)] B<sub>i+1,k&#x2212;1</sub>(x)"),
    note("Convention: 0/0 = 0. This handles repeated knots safely."),
    h2("6.3 Key Properties"),
    b("<b>Local support:</b> B<sub>i,k</sub>(x) is non-zero only for x &#x2208; [t<sub>i</sub>, t<sub>i+k</sub>]. "
      "This gives banded matrices — only k&#x2212;1 splines overlap at any point."),
    b("<b>Partition of unity:</b> &#x2211; B<sub>i,k</sub>(x) = 1 everywhere between t<sub>first</sub> and t<sub>last</sub>."),
    b("<b>Smoothness:</b> B<sub>i,k</sub> is C<sup>k&#x2212;2</sup>. For k=4: C<sup>2</sup> — twice differentiable everywhere "
      "except at knots with multiplicity > 1."),
    b("<b>Boundary BCs:</b> With k repeated boundary knots, only B<sub>0</sub> is nonzero at the left end "
      "and only B<sub>last</sub> at the right end. Dropping these two splines enforces "
      "zero boundary conditions automatically."),
    h2("6.4 Derivatives"),
    p("<b>First derivative:</b>"),
    p("dB<sub>i,k</sub>/dx = (k&#x2212;1) [ B<sub>i,k&#x2212;1</sub>/(t<sub>i+k&#x2212;1</sub>&#x2212;t<sub>i</sub>)  "
      "&#x2212;  B<sub>i+1,k&#x2212;1</sub>/(t<sub>i+k</sub>&#x2212;t<sub>i+1</sub>) ]"),
    p("<b>Second derivative:</b>  Apply the first-derivative formula twice. "
      "The library handles this automatically via <i>diff(order=2)</i>."),
    PageBreak(),
]

# ── Section 7: Library layout ────────────────────────────────────
story += [
    h1("7. The johntfoster/bspline Library — Repository Layout"),
    p("The repository at <b>https://github.com/johntfoster/bspline</b> provides "
      "a NumPy implementation of the Cox–de Boor algorithm with two Python files "
      "that are all you need:"),
    code("""
johntfoster/bspline/
│
├── bspline/               ← the Python package (what pip installs)
│   ├── __init__.py        ← makes 'import bspline' work
│   ├── bspline.py         ← class Bspline  +  memoize decorator
│   └── splinelab.py       ← augknt, aptknt, aveknt, knt2mlt, spcol
│
├── test/                  ← unit tests (good to read for expected behaviour)
├── README.md              ← usage examples
└── setup.py               ← pip packaging
"""),
    h2("Install"),
    code("""
pip install bspline          # from PyPI (simplest)

# OR from your forked repo:
git clone https://github.com/YOUR-USERNAME/bspline.git
cd bspline
pip install -e .             # editable: source changes take effect immediately
"""),
    h2("Standard imports at the top of every assignment file"),
    code("""
import numpy as np
import bspline
import bspline.splinelab as splinelab
from scipy.linalg import lu_factor, lu_solve, eigh
from numpy.polynomial.legendre import leggauss
import matplotlib.pyplot as plt
"""),
    PageBreak(),
]

# ── Section 8: Order convention ──────────────────────────────────
story += [
    h1("8. The Order Convention: Library p vs Assignment k  (READ THIS FIRST)"),
    p("The single most common source of bugs when using this library with the assignment PDF. "
      "They use different names for the same thing."),
    sp(5),
    tbl([
        ["Property", "Assignment PDF\n(de Boor notation)", "johntfoster/bspline\n(CS notation)"],
        ["Main symbol", "k", "p  (called 'order' in __init__)"],
        ["Polynomial degree", "k − 1", "p"],
        ["Cubic splines", "k = 4", "p = 3"],
        ["Boundary repeats per end", "k copies", "(p+1) copies total\n(augknt adds p, knots has 1)"],
        ["Number of splines\n(N total knots)", "N − k", "len(t) − p − 1"],
        ["Min order for 2nd derivative", "k ≥ 4", "p ≥ 3"],
    ], [4.5*cm, 5.5*cm, 5.5*cm]),
    sp(8),
    key("Assignment says k=4  →  pass p=3 to the library.  "
        "Count splines as  len(t) − p − 1,  not  N − k."),
    code("""
# THE TRANSLATION:
k_assign = 4                      # assignment notation
p_lib    = k_assign - 1           # = 3  → pass this to Bspline() and augknt()

# Verify they give the same number of splines:
inner = np.linspace(0, 20, 30)

# Assignment manual approach:
t_manual = np.concatenate([np.repeat(inner[0], k_assign),
                            inner[1:-1],
                            np.repeat(inner[-1], k_assign)])
n_sp_assign = len(t_manual) - k_assign

# Library approach:
t_lib    = splinelab.augknt(inner, p_lib)
n_sp_lib = len(t_lib) - p_lib - 1

print(n_sp_assign, n_sp_lib)   # both should print 32  ← same!
"""),
    PageBreak(),
]

# ── Section 9: Library API ───────────────────────────────────────
story += [h1("9. The johntfoster/bspline API — Every Method Explained")]

# 9.1 augknt
story += [
    libbar("9.1   splinelab.augknt(knots, order)  —  Build the knot vector  [FIRST CALL]"),
    sp(4),
    p("<b>Source (verbatim):</b>  "
      "return np.array( [knots[0]]*order  +  list(knots)  +  [knots[-1]]*order )"),
    p("<b>What it does:</b> Prepends <i>order</i> (= p) copies of the first knot and "
      "appends <i>order</i> copies of the last knot. "
      "Combined with the existing endpoint, each boundary gets p+1 = k copies total."),
    code("""
import numpy as np
import bspline.splinelab as splinelab

p     = 3                                     # cubic (k=4 in assignment)
inner = np.array([0., 5., 10., 15., 20.])    # 5 distinct physical points

t = splinelab.augknt(inner, p)
print(t)
# [ 0.  0.  0.  0.  5.  10.  15.  20.  20.  20.  20.]
#  ^-- p=3 prepended --^               ^-- p=3 appended --^
# Total length = 5 + 2*3 = 11
# n_basis = len(t) - p - 1 = 11 - 3 - 1 = 7
"""),
    libbox("This is the ONLY function from splinelab you MUST call. "
           "Everything else is optional."),
    sp(8),
]

# 9.2 Bspline init
story += [
    libbar("9.2   bspline.Bspline(knot_vector, order)  —  Create the basis object"),
    sp(4),
    p("<b>What it does:</b> Stores the knot vector and degree p. "
      "Immediately runs two dummy evaluations at x=0 to warm the memoisation cache."),
    p("<b>Create it ONCE and reuse</b> — the cache lives on the instance."),
    code("""
import bspline
import bspline.splinelab as splinelab

p     = 3
inner = np.linspace(0, 30, 40)
t     = splinelab.augknt(inner, p)

B = bspline.Bspline(t, p)           # ← CREATE ONCE at the top of your script
n_basis = len(t) - p - 1
print(f"Basis has {n_basis} functions")

# Reuse B for all matrix building, reconstruction, and plotting.
# DO NOT create a new Bspline() inside a loop — cache starts empty each time.
"""),
    sp(8),
]

# 9.3 __call__
story += [
    libbar("9.3   B(x)  —  All basis function values at one point x"),
    sp(4),
    p("<b>Returns:</b> 1-D array of length n_basis. Element i = B<sub>i</sub>(x). "
      "At most p+1 = 4 elements are non-zero (local support)."),
    p("<b>When to use it:</b> Evaluating a spline-expanded function at a single point, "
      "or building matrices one point at a time."),
    code("""
vals = B(2.5)                  # shape (n_basis,)
# vals[i] = B_i(2.5)
# Most are 0.0 — only ~4 are nonzero near x=2.5

# Reconstruct phi(r) at one point from coefficients c:
c = np.random.randn(n_basis)
phi_at_2_5 = np.sum(B(2.5) * c)

# Memoised: calling B(2.5) a second time is free (cached).
"""),
    sp(8),
]

# 9.4 d()
story += [
    libbar("9.4   B.d(x)  —  First derivatives of all basis functions  [FAST PATH]"),
    sp(4),
    p("<b>Returns:</b> 1-D array. Element i = dB<sub>i</sub>/dx at x."),
    p("<b>This is the fast path.</b> Uses a modified recursion (replaces the numerator "
      "in the last step with ±p). Memoised, same speed as B(x)."),
    code("""
dvals = B.d(3.7)               # shape (n_basis,)
# dvals[i] = dB_i/dx  at x = 3.7

# ── Assignment 5: kinetic energy contribution at Gauss point x, weight w ──
kinetic_contrib = 0.5 * w * dvals[j] * dvals[i]

# Use B.d(x), NOT B.diff(order=1)(x) — they give the same result
# but d() is faster because it takes the internal fast path.
"""),
    sp(8),
]

# 9.5 diff()
story += [
    libbar("9.5   B.diff(order=n)  —  Any-order derivative as a callable"),
    sp(4),
    p("<b>Returns:</b> A lambda function  f(x)  that evaluates the n-th derivative "
      "of ALL basis functions at x. "
      "Each differentiation step doubles the number of internal terms (2<sup>n</sup> terms total). "
      "Practical up to n=3."),
    code("""
D2 = B.diff(order=2)           # second-derivative function
d2vals = D2(4.1)               # shape (n_basis,)
# d2vals[i] = d^2 B_i / dx^2  at x = 4.1

# ── Assignment 4: fill the collocation matrix row by row ──────────
D2 = B.diff(order=2)
for row, ri in enumerate(collocation_points):
    A[row, :] = D2(ri)         # entire row from one call
    rhs[row]  = -ri * 4*np.pi * rho(ri)

# For order > p, diff() returns identically zero (correct behaviour):
D5 = B.diff(order=5)
print(D5(0.3))   # array of zeros
"""),
    warn("diff(order=1)(x)  and  d(x)  give identical results, but d(x) "
         "is faster. Always use d(x) for first derivatives."),
    sp(8),
]

# 9.6 collmat — THE KEY METHOD
story += [
    libbar("9.6   B.collmat(tau, deriv_order=0)  —  The collocation matrix  [KEY]"),
    sp(4),
    p("<b>Returns:</b> 2-D array of shape (len(tau), n_basis).  "
      "Element [i, j] = D<sup>deriv_order</sup> B<sub>j</sub>(tau<sub>i</sub>)."),
    p("<b>This is the most important method for your assignments.</b> "
      "It builds an entire matrix block in one vectorised call — far faster "
      "than looping over collocation points yourself."),
    code("""
# ── Most common patterns ──────────────────────────────────────────

# 1. Interior collocation matrix (second derivatives) — Assignment 4
all_knots = np.unique(t)
tau_int   = all_knots[1:-1]           # interior physical knots

A2 = B.collmat(tau_int, deriv_order=2)
# Shape: (N_int-2, n_basis)
# A2[i, j] = d^2 B_j/dr^2  at r = tau_int[i]
# → Paste into rows 1 to N_int-2 of your system matrix

# 2. Boundary condition rows
row_bc0  = B.collmat([all_knots[0]],  deriv_order=0)  # shape (1, n_basis)
row_bcR  = B.collmat([all_knots[-1]], deriv_order=0)  # shape (1, n_basis)
# row_bc0  will be [1, 0, 0, ...] because only B_0 nonzero at r=0
# row_bcR  will be [..., 0, 1]   because only B_last nonzero at r_max

# 3. Reconstruct function on a dense grid — MATRIX MULTIPLY
r_plot = np.linspace(0.01, r_max, 400)
A_plot = B.collmat(r_plot, deriv_order=0)    # shape (400, n_basis)
phi    = A_plot @ c                           # shape (400,)  — phi(r) values

# 4. Galerkin matrices — Assignment 5
#    Evaluate ALL basis functions at ALL Gauss points in one call
x_gauss, w_gauss = gl_on(a, b)             # ngl Gauss points on [a, b]
Bvals  = B.collmat(x_gauss, deriv_order=0) # shape (ngl, n_basis)
dBvals = B.collmat(x_gauss, deriv_order=1) # shape (ngl, n_basis)
# Bvals[:, j]  = B_j at all Gauss points
# dBvals[:, j] = dB_j/dr at all Gauss points
"""),
    key("Use  A_plot @ c  (matrix-vector multiply) instead of a loop over basis functions "
        "when reconstructing the potential on a dense grid. It is 100x faster."),
    sp(8),
]

# 9.7 splinelab utilities
story += [
    libbar("9.7   splinelab utilities: aptknt · aveknt · knt2mlt · spcol"),
    sp(4),
    p("These are rarely needed for your assignments but documented for completeness."),
    code("""
# aptknt(tau, order) — knot vector fitted to collocation sites
# Use when you have specific sites where the equation must be satisfied
# and want the knot vector to match them. For your work, augknt is simpler.
t_apt = splinelab.aptknt(np.linspace(0,20,15), p=3)

# aveknt(t, k) — running average of k successive knot entries
# Used internally by aptknt. Rarely called directly.
avg = splinelab.aveknt(np.array([0.,1.,2.,3.,4.]), k=3)
# → [1.0, 2.0, 3.0]  (averages of [0,1,2], [1,2,3], [2,3,4])

# knt2mlt(t) — count how many times each knot has appeared before
m = splinelab.knt2mlt(np.array([0.,0.,0.,0.,5.,10.,20.,20.,20.,20.]))
# → [0, 1, 2, 3, 0, 0, 0, 1, 2, 3]

# spcol(knots, order, tau) — collocation matrix with multiplicity-aware derivatives
# Like B.collmat() but automatically uses higher derivatives at repeated sites.
# Only needed if you want to enforce both value AND derivative at the same point.
A = splinelab.spcol(t, p=3, tau=np.unique(t)[1:-1])  # same as B.collmat(tau)
"""),
    sp(8),
]

# 9.8 memoize
story += [
    libbar("9.8   The memoize Cache — Why You Create Bspline Only Once"),
    sp(4),
    p("The <b>memoize</b> decorator (from bspline.py) caches the return value of "
      "any call based on the arguments. The first call computes and stores the result. "
      "All subsequent calls with the same argument retrieve it instantly."),
    code("""
# From bspline.py (simplified):
# @memoize is applied to both __call__ and d:
#
# First call:  B(2.5)  → runs full Cox-de Boor recursion → stores in cache
# Second call: B(2.5)  → returns cached value, no recomputation
#
# The cache key is the argument value (xi must be hashable, i.e. a float).
# The cache is stored on the Bspline INSTANCE.

# CORRECT: create once, reuse
B = bspline.Bspline(t, p)
for xi in gauss_points:
    vals = B(xi)       # second iteration: cache hit for any repeated xi

# WRONG: creates new object each iteration — cache is always empty
for xi in gauss_points:
    B_tmp = bspline.Bspline(t, p)   # DON'T DO THIS
    vals = B_tmp(xi)
"""),
    warn("The memoize cache stores floats as keys. Passing numpy scalars vs Python floats "
         "can sometimes create separate cache entries. "
         "Convert Gauss points to Python floats if you see unexpected slowness: "
         "float(xi)."),
    PageBreak(),
]

# ════════════════════════════════════════════════════════════════════
# PART C — ASSIGNMENTS
# ════════════════════════════════════════════════════════════════════
story += [Paragraph("PART C — ASSIGNMENTS", S("PC", fontSize=16,
          textColor=colors.white, backColor=DARK, fontName="Helvetica-Bold",
          alignment=TA_CENTER, spaceBefore=6, spaceAfter=6, borderPad=8)),
    PageBreak()]

# ── Section 10: Assignment 4 ─────────────────────────────────────
story += [
    h1("10. Assignment 4 — Poisson Collocation"),
    h2("10.1 The Physics"),
    p("We want the electrostatic potential V(r) from a spherically symmetric charge &#x03C1;(r). "
      "With the substitution &#x03C6;(r) = r&#x00D7;V(r), the 3-D Poisson equation reduces to "
      "a 1-D second-order ODE (with 4&#x03C0;&#x03B5;<sub>0</sub> = 1):"),
    p("<b>d&#x00B2;&#x03C6;/dr&#x00B2; = &#x2212; 4&#x03C0; r &#x03C1;(r)</b>"),
    p("Boundary conditions:  &#x03C6;(0) = 0  (regularity at origin);  "
      "&#x03C6;(r&#x2192;&#x221E;) = Q  (total charge)."),
    h2("10.2 Method — Step by Step"),
    b("Build knot vector t with augknt."),
    b("Create Bspline object B."),
    b("Get collocation matrix of second derivatives:  A2 = B.collmat(tau, deriv_order=2)."),
    b("Assemble system matrix: row 0 = BC at r=0; interior rows = A2; last row = BC at r_max."),
    b("Build RHS: row 0 = 0; interior = &#x2212;r&#x1D62;&#x00D7;4&#x03C0;&#x03C1;(r&#x1D62;); last = Q."),
    b("LU-factorise once; solve for each charge distribution."),
    b("Reconstruct:  phi = B.collmat(r_plot) @ c;  V = phi / r."),
    h2("10.3 Library Calls Mapped to Each Step"),
    tbl([
        ["Step", "Library call", "Returns"],
        ["Build knot vector", "splinelab.augknt(inner, p=3)", "1-D array t"],
        ["Create basis", "bspline.Bspline(t, p=3)", "Bspline object B"],
        ["Second-deriv matrix", "B.collmat(tau_int, deriv_order=2)", "shape (N-2, n_basis)"],
        ["BC row at r=0", "B.collmat([0.], deriv_order=0)", "shape (1, n_basis) = [1,0,...,0]"],
        ["BC row at r_max", "B.collmat([r_max], deriv_order=0)", "shape (1, n_basis) = [...,0,1]"],
        ["Solve system", "lu_factor(A) then lu_solve((lu,piv), rhs)", "coefficient vector c"],
        ["Reconstruct phi", "B.collmat(r_plot) @ c", "phi values on r_plot"],
    ], [3*cm, 7*cm, 5*cm]),
    sp(8),
    h2("10.4 Complete Working Code"),
    code("""
import numpy as np
import bspline
import bspline.splinelab as splinelab
from scipy.linalg import lu_factor, lu_solve
import matplotlib.pyplot as plt

# ── Parameters ────────────────────────────────────────────────────
p_lib = 3          # library degree  (= assignment k-1 = 4-1)
r_max = 20.0
Q     = 1.0        # total charge
N_pts = 35         # distinct physical knot points

# ── Step 1: Knot vector ────────────────────────────────────────────
inner = np.linspace(0, r_max, N_pts)
t     = splinelab.augknt(inner, p_lib)
n_basis = len(t) - p_lib - 1        # number of B-splines

# ── Step 2: Create basis object (ONCE) ───────────────────────────
B = bspline.Bspline(t, p_lib)

# ── Step 3: Collocation points (distinct interior knots) ──────────
all_knots = np.unique(t)             # length N_pts
tau_int   = all_knots[1:-1]         # interior, length N_pts-2

# ── Step 4: Assemble system matrix ────────────────────────────────
A_sys = np.zeros((n_basis, n_basis))

# Row 0: phi(r=0) = 0
A_sys[0, :] = B.collmat([all_knots[0]],  deriv_order=0)

# Interior rows: d^2 phi / dr^2 = -r * 4*pi*rho
A_int = B.collmat(tau_int, deriv_order=2)     # shape (N_pts-2, n_basis)
A_sys[1:len(tau_int)+1, :] = A_int

# Last row: phi(r_max) = Q
A_sys[-1, :] = B.collmat([all_knots[-1]], deriv_order=0)

# ── Step 5: LU factorise ONCE ────────────────────────────────────
lu, piv = lu_factor(A_sys)

# ── Step 6: Solve for each distribution ──────────────────────────
R = 5.0
def rho_sphere(r):
    V = (4/3)*np.pi*R**3
    return np.where(r <= R, Q/V, 0.0)

def rho_shell(r, R1=4., R2=8.):
    V = (4/3)*np.pi*(R2**3 - R1**3)
    return np.where((r >= R1) & (r <= R2), Q/V, 0.0)

def rho_hydrogen(r):
    return 4.0 * np.exp(-2*r)       # 4*pi*|psi_1s|^2, psi_1s = exp(-r)/sqrt(pi)

def build_rhs(rho_func):
    rhs = np.zeros(n_basis)
    rhs[0]  = 0.0                   # phi(0) = 0
    for idx, ri in enumerate(tau_int):
        rhs[idx+1] = -ri * 4*np.pi * rho_func(ri)
    rhs[-1] = Q                     # phi(r_max) = Q
    return rhs

c_sphere = lu_solve((lu, piv), build_rhs(rho_sphere))
c_shell  = lu_solve((lu, piv), build_rhs(rho_shell))
c_hydro  = lu_solve((lu, piv), build_rhs(rho_hydrogen))

# ── Step 7: Reconstruct and plot ─────────────────────────────────
r_plot = np.linspace(0.02, r_max, 500)
A_plot = B.collmat(r_plot, deriv_order=0)    # shape (500, n_basis)

V_sphere = (A_plot @ c_sphere) / r_plot
V_shell  = (A_plot @ c_shell)  / r_plot
V_hydro  = (A_plot @ c_hydro)  / r_plot

# ── Analytical check for sphere ───────────────────────────────────
V_exact = np.where(r_plot <= R,
                   Q/R * (1.5 - 0.5*(r_plot/R)**2),
                   Q/r_plot)
print(f"Max error: {np.max(np.abs(V_sphere - V_exact)):.2e}")

fig, axes = plt.subplots(1, 3, figsize=(13, 4))
for ax, V, title in zip(axes,
                         [V_sphere, V_shell, V_hydro],
                         ["Sphere", "Shell", "Hydrogen 1s"]):
    ax.plot(r_plot, V, "b-", label="Numerical")
    ax.set_title(title); ax.set_xlabel("r [Bohr]"); ax.grid(alpha=0.3)
axes[0].plot(r_plot, V_exact, "r--", label="Analytical"); axes[0].legend()
plt.tight_layout(); plt.savefig("poisson_all.png", dpi=150)
"""),
    h2("10.5 Analytical Solutions"),
    p("<b>Sphere</b> (R, Q=1):  V = Q/(2R)(3&#x2212;r&#x00B2;/R&#x00B2;) for r&#x2264;R;  V = Q/r for r&gt;R"),
    p("<b>Shell</b> (R<sub>1</sub>, R<sub>2</sub>, Q=1):  "
      "V = const = Q/(4&#x03C0;R<sub>1</sub>) for r&lt;R<sub>1</sub>;  V = Q/r for r&gt;R<sub>2</sub>"),
    p("<b>Hydrogen 1s</b>:  V(r) = 1/r &#x2212; e<sup>&#x2212;2r</sup>(1/r + 1)"),
    PageBreak(),
]

# ── Section 11: Assignment 5 ─────────────────────────────────────
story += [
    h1("11. Assignment 5 — Hydrogen Eigenvalue Problem"),
    h2("11.1 Physics and Galerkin Formulation"),
    p("The radial Schr&#x00F6;dinger equation (Hartree units, &#x0127; = m<sub>e</sub> = 1):"),
    p("[ &#x2212;&#x00BD; d&#x00B2;/dr&#x00B2; + &#x2113;(&#x2113;+1)/(2r&#x00B2;) &#x2212; Z/r ] "
      "P<sub>n&#x2113;</sub> = E P<sub>n&#x2113;</sub>"),
    p("Expand P = &#x2211; c<sub>i</sub>B<sub>i</sub>, multiply by B<sub>j</sub>, integrate "
      "&#x2192; generalised eigenvalue problem <b>H c = E S c</b>:"),
    p("H<sub>ij</sub> = &#x00BD;&#x222B;B'<sub>j</sub>B'<sub>i</sub>dr  "
      "+ &#x2113;(&#x2113;+1)/2&#x222B;B<sub>j</sub>r<sup>&#x2212;2</sup>B<sub>i</sub>dr  "
      "&#x2212; Z&#x222B;B<sub>j</sub>r<sup>&#x2212;1</sup>B<sub>i</sub>dr"),
    p("S<sub>ij</sub> = &#x222B;B<sub>j</sub>B<sub>i</sub>dr"),
    h2("11.2 Library Calls for Matrix Construction"),
    tbl([
        ["Matrix element", "Library calls", "Note"],
        ["Kinetic  ½∫B'j B'i", "B.collmat(x_gl, deriv_order=1)\n→ dBvals[:,j] * dBvals[:,i]",
         "Use d() for speed at single points;\ncollmat is better for many points"],
        ["Centrifugal  ℓ(ℓ+1)/2 ∫Bj r⁻² Bi",
         "B.collmat(x_gl, deriv_order=0)\n→ Bvals[:,j] / x_gl² * Bvals[:,i]",
         "Avoid evaluating at r=0!"],
        ["Coulomb  −Z ∫Bj r⁻¹ Bi",
         "B.collmat(x_gl, deriv_order=0)\n→ Bvals[:,j] / x_gl * Bvals[:,i]",
         ""],
        ["Overlap  ∫Bj Bi",
         "B.collmat(x_gl, deriv_order=0)\n→ Bvals[:,j] * Bvals[:,i]",
         "Gauss weights sum to interval length"],
    ], [3.5*cm, 7*cm, 5*cm]),
    sp(6),
    h2("11.3 Complete Working Code"),
    code("""
import numpy as np
import bspline
import bspline.splinelab as splinelab
from scipy.linalg import eigh
from numpy.polynomial.legendre import leggauss
import matplotlib.pyplot as plt

# ── Parameters ────────────────────────────────────────────────────
p_lib = 3;  Z = 1;  ell = 0
r_max = 30.0;  N_pts = 50;  ngl = 5

# ── Knot vector and basis ──────────────────────────────────────────
inner = np.linspace(0, r_max, N_pts)
t     = splinelab.augknt(inner, p_lib)
B     = bspline.Bspline(t, p_lib)      # CREATE ONCE
n_basis = len(t) - p_lib - 1
n_act   = n_basis - 2                  # drop first and last (BCs)

# ── Gauss-Legendre quadrature ─────────────────────────────────────
gl_z, gl_w = leggauss(ngl)
t_uniq = np.unique(t)

H_mat = np.zeros((n_act, n_act))
S_mat = np.zeros((n_act, n_act))

for m in range(len(t_uniq) - 1):
    a, b = t_uniq[m], t_uniq[m+1]
    if a == b: continue

    x_pts = 0.5*(b-a)*gl_z + 0.5*(b+a)    # Gauss pts on [a, b]
    w_pts = 0.5*(b-a)*gl_w

    # ── Evaluate ALL basis functions at ALL Gauss points (vectorised)
    Bv  = B.collmat(x_pts, deriv_order=0)  # shape (ngl, n_basis)
    dBv = B.collmat(x_pts, deriv_order=1)  # shape (ngl, n_basis)

    for ii in range(n_act):
        i = ii + 1    # actual basis index (active = 1 to n_basis-2)
        for jj in range(n_act):
            j = jj + 1
            Bj = Bv[:,j]; Bi = Bv[:,i]
            dBj=dBv[:,j]; dBi=dBv[:,i]

            kin  = np.sum(w_pts * 0.5 * dBj * dBi)
            cent = np.sum(w_pts * 0.5*ell*(ell+1) / x_pts**2 * Bj * Bi)
            coul = np.sum(w_pts * (-Z) / x_pts * Bj * Bi)
            over = np.sum(w_pts * Bj * Bi)

            H_mat[ii,jj] += kin + cent + coul
            S_mat[ii,jj] += over

# ── Solve generalised eigenvalue problem ──────────────────────────
evals, evecs = eigh(H_mat, S_mat)

print(f"Bound states for ell={ell}, Z={Z}:")
for idx, E in enumerate(evals[:8]):
    if E >= 0: break
    n = idx + ell + 1
    E_ex = -Z**2 / (2*n**2)
    print(f"  n={n}: E={E:.6f} Ha  exact={E_ex:.6f} Ha  err={abs(E-E_ex):.1e}")

# ── Reconstruct and normalise ground state ────────────────────────
r_plot = np.linspace(0.01, r_max, 500)
A_pl   = B.collmat(r_plot, deriv_order=0)   # shape (500, n_basis)
c_gs   = evecs[:, 0]                         # ground state coefficients
P_gs   = A_pl[:, 1:-1] @ c_gs               # shape (500,)  — skip BC splines
norm   = np.trapz(P_gs**2, r_plot)
P_gs  /= np.sqrt(norm)

P_exact = 2*r_plot*np.exp(-r_plot)           # H 1s: P(r) = 2r exp(-r)
plt.figure(figsize=(7,4))
plt.plot(r_plot, P_gs,    "b-",  label="B-spline")
plt.plot(r_plot, P_exact, "r--", label="Exact 1s")
plt.xlabel("r [Bohr]"); plt.ylabel("P(r)"); plt.legend()
plt.title(f"Hydrogen radial function, ell={ell}")
plt.tight_layout(); plt.savefig("hydrogen_gs.png", dpi=150)
"""),
    h2("11.4 Exponential Knot Sequence (Better for Hydrogen)"),
    p("Hydrogen wave functions decay as e<sup>&#x2212;r/n</sup>. "
      "An exponential knot sequence concentrates points near r=0 "
      "where the function changes most rapidly."),
    code("""
# Exponential inner knots — dense near origin, sparse far out
N_exp    = 40
r_min_in = 0.01
inner_exp = np.exp(np.linspace(np.log(r_min_in), np.log(r_max), N_exp))
inner_exp = np.concatenate([[0.0], inner_exp])   # prepend r=0
t_exp = splinelab.augknt(inner_exp, p_lib)
# This gives much better accuracy for n=3,4,5 states with fewer knots.
"""),
    PageBreak(),
]

# ── Section 12: Assignment 6 ─────────────────────────────────────
story += [
    h1("12. Assignment 6 — Self-Consistent Field for Many-Electron Atoms"),
    h2("12.1 The SCF Loop"),
    p("Assignment 6 plugs Assignments 4 and 5 together inside an iteration loop. "
      "The library calls are identical — the only new code is computing &#x03C1; "
      "from wave functions and adding V<sub>ee</sub> to the H matrix."),
    b("Start: solve hydrogen-like eigenvalue (V<sub>ee</sub>=0) for each occupied (n,&#x2113;)."),
    b("Normalise orbitals P<sub>n&#x2113;</sub>(r).  Check: 4&#x03C0;&#x222B;&#x03C1;r&#x00B2;dr = N<sub>elec</sub>."),
    b("Solve Poisson (Assign. 4 code, unchanged) for V<sup>dir</sup><sub>ee</sub>(r)."),
    b("Add Slater exchange: V<sup>exch</sup> = &#x2212;3[3&#x03C1;/(8&#x03C0;)]<sup>1/3</sup>."),
    b("Add V<sub>ee</sub> term to H matrix inner loop (one extra np.sum per pair)."),
    b("Mix: V<sub>ee</sub> &#x2190; (1&#x2212;&#x03B7;)V<sub>ee,new</sub> + &#x03B7;V<sub>ee,old</sub>  with &#x03B7;&#x2248;0.4."),
    b("Repeat until max |&#x0394;E<sub>n&#x2113;</sub>| &lt; 10<sup>&#x2212;5</sup> Ha (&#x2248;30 iterations for He, 60 for Ne)."),
    h2("12.2 Aufbau Orbital Filling"),
    code("""
# Filling order for neutral atoms:
aufbau = [
    (1,0,2),  # 1s  — 2 electrons
    (2,0,2),  # 2s
    (2,1,6),  # 2p  — 6 electrons
    (3,0,2),  # 3s
    (3,1,6),  # 3p
    (4,0,2),  # 4s   ← fills BEFORE 3d (Madelung rule)
    (3,2,10), # 3d  — 10 electrons
    (4,1,6),  # 4p
]  # each tuple: (n, ell, max_electrons)

def get_config(Z_atom):
    remaining = Z_atom
    config = []
    for (n, l, cap) in aufbau:
        if remaining <= 0: break
        occ = min(remaining, cap)
        config.append((n, l, occ))
        remaining -= occ
    return config

print(get_config(2))    # He:  [(1,0,2)]
print(get_config(10))   # Ne:  [(1,0,2),(2,0,2),(2,1,6)]
print(get_config(19))   # K:   [... (4,0,1)]   — 19th electron in 4s, not 3d!
"""),
    h2("12.3 Charge Density, Exchange Potential, Total Energy"),
    code("""
# ── Charge density from occupied orbitals ─────────────────────────
def compute_rho(config, orbitals, r_grid):
    rho = np.zeros_like(r_grid)
    for (n, l, N_e) in config:
        P    = orbitals[(n,l)]                    # shape (len(r_grid),)
        norm = np.trapz(P**2, r_grid)
        P   /= np.sqrt(norm)                      # normalise
        rho += N_e * (P/r_grid)**2 / (4*np.pi)   # add contribution
    check = 4*np.pi * np.trapz(rho * r_grid**2, r_grid)
    assert abs(check - sum(N for _,_,N in config)) < 0.01, f"rho normalisation failed: {check:.3f}"
    return rho

# ── Slater exchange ───────────────────────────────────────────────
def V_exchange(rho):
    return -3.0 * (3.0 * np.maximum(rho, 1e-30) / (8.0*np.pi))**(1.0/3.0)

# ── Add V_ee to H matrix elements (inside interval loop) ──────────
from scipy.interpolate import interp1d
V_ee_fn = interp1d(r_grid, V_dir + V_exch, kind='linear',
                   fill_value=0., bounds_error=False)
# Inside the ii/jj loop:
V_ee_pts = V_ee_fn(x_pts)                    # V_ee at Gauss points
vee_contrib = np.sum(w_pts * Bv[:,j] * V_ee_pts * Bv[:,i])
H_mat[ii,jj] += vee_contrib

# ── Total energy (no double counting) ────────────────────────────
def total_energy(config, E_orbitals, orbitals, V_ee, r_grid):
    E_tot = 0.0
    for (n, l, N_e) in config:
        P  = orbitals[(n,l)]
        Vee_exp = np.trapz(P**2 * V_ee, r_grid)
        E_tot  += N_e * (E_orbitals[(n,l)] - 0.5 * Vee_exp)
    return E_tot
"""),
    h2("12.4 Convergence Check Values"),
    tbl([
        ["Atom", "Orbital", "Start (no V_ee)", "Converged (with V_ee)", "Source"],
        ["He (Z=2)", "1s", "−2.000 Ha", "≈ −0.740 Ha", "Assignment sheet"],
        ["Ne (Z=10)", "1s", "−50.0 Ha",  "≈ −31.4 Ha",  "Assignment sheet"],
        ["Ne (Z=10)", "2s", "−12.5 Ha",  "≈ −1.53 Ha",  "Assignment sheet"],
        ["Ne (Z=10)", "2p", "−12.5 Ha",  "≈ −0.68 Ha",  "Assignment sheet"],
    ], [3*cm, 2.5*cm, 4*cm, 4.5*cm, 3*cm]),
    sp(6),
    warn("He ionisation energy from this method: ≈ 0.70 Ha ≈ 19 eV. "
         "Experimental: 24.6 eV. The Slater exchange approximation "
         "is less accurate for atoms with few electrons."),
    PageBreak(),
]

# ════════════════════════════════════════════════════════════════════
# PART D — REFERENCE
# ════════════════════════════════════════════════════════════════════
story += [Paragraph("PART D — REFERENCE", S("PD", fontSize=16,
          textColor=colors.white, backColor=DARK, fontName="Helvetica-Bold",
          alignment=TA_CENTER, spaceBefore=6, spaceAfter=6, borderPad=8)),
    PageBreak()]

# ── Section 13: Debugging checklist ──────────────────────────────
story += [
    h1("13. Debugging Checklist"),
    h2("Assignment 4"),
    b("&#x2610; V(r) matches 1/r outside the sphere analytically?"),
    b("&#x2610; Row 0 of A enforces &#x03C6;(0)=0?  (should be [1, 0, 0, ...])"),
    b("&#x2610; Last row of A enforces &#x03C6;(r_max)=Q?"),
    b("&#x2610; RHS has both the factor r AND the factor 4&#x03C0;?"),
    b("&#x2610; V = phi/r, not V = phi?"),
    b("&#x2610; p_lib = 3 passed to augknt and Bspline (not k=4)?"),
    b("&#x2610; collmat used with deriv_order=2 for interior rows?"),
    h2("Assignment 5"),
    b("&#x2610; Active splines are indices 1 to n_basis-2  (drop first and last)?"),
    b("&#x2610; Kinetic term uses dBj * dBi (integration by parts), NOT d&#x00B2;Bj * Bi?"),
    b("&#x2610; eigh called (not eig) — needs symmetric H and S?"),
    b("&#x2610; Ground state energy within 10<sup>&#x2212;4</sup> of &#x2212;0.5 Ha for hydrogen?"),
    b("&#x2610; Coulomb term is &#x2212;Z/r (negative — attractive)?"),
    b("&#x2610; r_max large enough that P(r_max) &#x2248; 0?"),
    b("&#x2610; Avoid evaluating 1/r&#x00B2; or 1/r at r=0 (use Gauss points, never at 0)?"),
    h2("Assignment 6"),
    b("&#x2610; Orbitals normalised before computing &#x03C1;?  (&#x222B;P&#x00B2;dr = 1)"),
    b("&#x2610; 4&#x03C0;&#x222B;&#x03C1;r&#x00B2;dr = N<sub>elec</sub>  (charge conservation)?"),
    b("&#x2610; Poisson BCs: &#x03C6;(0)=0, &#x03C6;(r_max)=N<sub>occ</sub>?  (not Q=1 as in Assign. 4)"),
    b("&#x2610; Direct potential is positive at large r (repulsive from electrons)?"),
    b("&#x2610; Exchange potential is negative everywhere (attractive correction)?"),
    b("&#x2610; Mixing applied: V<sub>new</sub> = (1&#x2212;&#x03B7;)V<sub>new</sub> + &#x03B7;V<sub>old</sub>?"),
    b("&#x2610; He converges to orbital energy &#x2248; &#x2212;0.74 Ha after ~30 iterations?"),
    PageBreak(),
]

# ── Section 14: What library does NOT do ─────────────────────────
story += [
    h1("14. What the Library Does NOT Do"),
    p("The library handles the B-spline maths. Everything physics-specific is yours."),
    sp(4),
    tbl([
        ["You write this yourself", "Library provides this"],
        ["Charge density ρ(r) definitions", "augknt — knot vector construction"],
        ["Boundary condition rows in matrix", "Bspline(t,p) — basis object"],
        ["RHS vector −r×4π×ρ", "collmat() — matrix of values/derivatives"],
        ["Call scipy to solve the system", "B(x), d(x), diff(n) — pointwise evaluation"],
        ["Gauss-Legendre quadrature loop", "Memoisation for repeated evaluations"],
        ["Galerkin H and S matrix assembly", "plot(), dplot() — quick visualisation"],
        ["Normalise eigenvectors from eigh", ""],
        ["Compute ρ from wave functions (A6)", ""],
        ["SCF convergence loop (A6)", ""],
        ["Slater exchange potential (A6)", ""],
    ], [9*cm, 8*cm]),
    sp(8),
    note("The library does about 20% of the work — the elegant, fiddly B-spline maths. "
         "Your 80% is the physics: boundary conditions, PDEs, integrands, and iteration loops."),
    PageBreak(),
]

# ── Section 15: Quick-reference sheet ───────────────────────────
story += [
    h1("15. Quick-Reference Formula Sheet"),
    h2("Hartree Atomic Units"),
    p("Length: a<sub>0</sub> = 0.529 &#x212B;  |  Energy: 1 Ha = 27.211 eV  |  "
      "&#x0127; = m<sub>e</sub> = e = 4&#x03C0;&#x03B5;<sub>0</sub> = 1"),
    p("Bound state energies of hydrogen:  E<sub>n</sub> = &#x2212;Z&#x00B2;/(2n&#x00B2;) Ha"),
    h2("Library Order Convention"),
    p("Assignment k=4  &#x2194;  Library p=3.  "
      "n_basis = len(t) &#x2212; p &#x2212; 1.  "
      "Active splines: indices 1 to n_basis&#x2212;2."),
    h2("Poisson (φ=rV, 4πε₀=1)"),
    p("d&#x00B2;&#x03C6;/dr&#x00B2; = &#x2212;4&#x03C0;r&#x03C1;(r).  "
      "BC: &#x03C6;(0)=0, &#x03C6;(&#x221E;)=Q.  "
      "V(r) = &#x03C6;(r)/r."),
    h2("Galerkin H Matrix Elements (Hartree units)"),
    p("H<sub>ij</sub> = &#x00BD;&#x222B;B'<sub>j</sub>B'<sub>i</sub>dr  "
      "+ &#x2113;(&#x2113;+1)/2&#x222B;B<sub>j</sub>r<sup>&#x2212;2</sup>B<sub>i</sub>dr  "
      "&#x2212; Z&#x222B;B<sub>j</sub>r<sup>&#x2212;1</sup>B<sub>i</sub>dr  "
      "+ &#x222B;B<sub>j</sub>V<sub>ee</sub>B<sub>i</sub>dr"),
    h2("Gauss-Legendre on [a,b]"),
    p("x = &#x00BD;(b&#x2212;a)z + &#x00BD;(b+a);  w = &#x00BD;(b&#x2212;a)w<sub>GL</sub>.  "
      "Use p+1 = 4 points per interval minimum."),
    h2("Slater Exchange"),
    p("V<sup>exch</sup>(r) = &#x2212;3[3&#x03C1;/(8&#x03C0;)]<sup>1/3</sup>  (negative, attractive)"),
    h2("SCF Mixing"),
    p("V<sub>new</sub> &#x2190; (1&#x2212;&#x03B7;)V<sub>new</sub> + &#x03B7;V<sub>old</sub>,  &#x03B7;=0.4.  "
      "Converge when max|&#x0394;E<sub>n&#x2113;</sub>| &lt; 10<sup>&#x2212;5</sup> Ha."),
    h2("Total Energy (no double counting)"),
    p("E<sub>total</sub> = &#x2211;<sub>i</sub> N<sub>i</sub> [E<sub>i</sub> "
      "&#x2212; &#x00BD; &#x27E8;P<sub>i</sub>|V<sub>ee</sub>|P<sub>i</sub>&#x27E9;]"),
    sp(10), hr(), sp(6),
    p("<b>You have everything you need.</b>  "
      "Start with augknt &#x2192; Bspline &#x2192; collmat for Assignment 4. "
      "Add d() and Gauss quadrature for Assignment 5. "
      "Wrap in a convergence loop for Assignment 6. "
      "Good luck!"),
]

# ── BUILD ─────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    "/mnt/user-data/outputs/Complete_BSpline_Physics_Guide.pdf",
    pagesize=A4,
    leftMargin=2.2*cm, rightMargin=2.2*cm,
    topMargin=2.5*cm,  bottomMargin=2.5*cm,
    title="B-Splines & Atomic Physics — Complete Integrated Guide",
    author="Devendra",
)
doc.build(story)
print("Master guide built successfully.")
