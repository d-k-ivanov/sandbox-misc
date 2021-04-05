use std::thread;

fn main()
{
    // Creating thread and run anonimous function
    let handler = thread::spawn(||
        {
            println!("I'm child thread");
        }
    );

    // Main thread
    println!("I'm main thread");
    handler.join().unwrap();
}
