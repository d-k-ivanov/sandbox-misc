fn main()
{
    // Object allocation on the heap
    let a = String::from("Hello");
    // Change ownership: moving
    let b = a;

    // Compilation errors: "value used here after move"
    // let c = a;
    // println!("{}", a);

    println!("{}", b);
}
