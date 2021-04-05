/// Sums two values.
///
/// # Examples
///
/// ```
/// let arg1 = 6;
/// let arg2 = 1;
/// let answer = testproc::add(arg1, arg2);
///
/// assert_eq!(add(6, 1), answer);
/// ```
fn add(a: u32, b: u32) -> u32
{
    a + b
}

#[test]
fn adder_tests()
{
    assert_eq!(add(2, 2), 4);
    assert_ne!(add(2, 2), 6);
}

/// Main function.
fn main()
{
    println!("Data = {}", add(1, 2));
    println!("Data = {}", add(10, 20));
    println!("Data = {}", add(5, 6));
    // println!("Data = {}", add(1.1, 2.2));
    // println!("Data = {}", add(0.1, -0.2));
    println!("Data = {}", add(0, 0));
}
