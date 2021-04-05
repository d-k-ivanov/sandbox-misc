fn do_smth(a: String)
{
    // Ownership in the function scope
    println!("{}", a);
}

fn main()
{
    let a = String::from("Hello");
    // Moving the object to the function scope
    do_smth(a);

    // Compilation error: already moved : "value used here after move"
    // let b = a;
}
