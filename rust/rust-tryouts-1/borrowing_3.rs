fn do_smth(a: &String)
{
    // Unmutable operation
    println!("{}", a);
}

fn main()
{
    let a = String::from("Hello");
    // Borrwing
    do_smth(&a);
    // Ovnership kept
    println!("{}", a);
}

/*
fn main()
{
    let mut s = String::from("hello");
    let r1 = &mut s;
    /// cannot borrow `s` as mutable more than once at a time
    let r2 = &mut s;
    println!("{}, {}", r1, r2);
}
*/
