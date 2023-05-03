# EECS-Tools Documentation

This documentation lists and explains all the functions implemented in this repository. The functions are organized into four files: `Digital.py`, `Dynamic.py`, `Steady.py`, and `Util.py`. There is also a `__config__.py` file for configuration. 

---

## `__config__.py` Configuration

This configuration file contains the following variables that control the program's behavior: 

### `VERBOSE_DEFAULT: bool`

When set to `True`, functions with the decorator (function annotation) `detect_verbose` prints out the returned results after their executions. 

---

## `Digital.py` 

No implementation so far. 

--- 

## `Dynamic.py` 

No implementation so far. 

---

## `Steady.py` 

### `R(v: float=None, i: float=None, p: float=None) -> float`

Computes the resistance, given any two of voltage `v`, current `i`, and power `p`. 

### `G(v: float=None, i:float=None, p:float=None) -> float`

Computes the conductance, given any two of voltage, current, and power

### `V(r: float=None, i: float=None, p: float=None, c: float=None, q: float=None, l: float=None, di: float=None) -> float:`

Computes the voltage, given the parameters

### `I(r: float=None, v: float=None, p: float=None) -> float`

Computes the current, given any two of resistance, voltage, and power

### `P(r: float=None, v: float=None, i: float=None) -> float`

Computes the power, given any two of resistance, voltage, and current

### `C(v: float=None, q: float=None) -> float`

Computes the capacitance of a linear capacitor, given the voltage and charge

### `Q(v: float=None, c: float=None) -> float`

Computes the charge stored on a linear capacitor, given the voltage and capacitance

### `E(c: float=None, v: float=None, i: float=None,p: float=None,r: float=None, t: float=None, l: float=None,) -> float:`

Computes the energy, given the parameters 



---

## `Util.py` 

Functions in `Util.py` are more generally purposed. They are mostly helper functions or math-related functions, listed below: 

### `inv_sum_inv(values: list[float]) -> float`

Returns the inverse of the sum of the inverse of the values contained in the input list `values`. 

### `degree_to_radian(degree: float) -> float`

Converts degree to radian by calling `math.radians()`

### `radian_to_degree(radian: float) -> float`

Converts radian to degree by calling `math.degrees()`

### `phasor_to_rectangular(phasor: tuple[float]) -> tuple[float]`

Converts the input `phasor = (magnitude, angle)`, where `angle` is in radian, into rectangular coordinate `(real, imag)` on the complex plane. 

### `rectangular_to_phasor(coord: tuple[float]) -> tuple[float]`

Converts the input `coord = (real, imag)` into a phasor `(magnitude, angle)`, where `angle` is in radian. 

### `complex_arithmetic(complex1: tuple[float], operator: str, complex2: tuple[float]) -> tuple[float]`

Performs complex arithmetic of the inputs `complex1` and `complex2`, both in the format of `(real, imag)`, using the operation given by `operator`. `operator` can take the following values: 

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division

### `(phasor1: tuple[float], operator: str, phasor2: tuple[float]) -> tuple[float]`

Performs complex arithmetic of the inputs `phasor1` and `phasor2`, both in the format of `(magnitude, angle)`, where `angle` is in radian, using the operation given by `operator`. `operator` can take the following values: 

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division


