use std::sync::mpsc::channel;
use std::thread;

fn main()
{
    // Creating a channel
    let (sender, receiver) = channel();

    // Creating a new thread and moving object to that thread
    thread::spawn(move ||
        {
        let hello = String::from("Hello");
        sender.send(hello).unwrap();
        // Compilation error: value used here after move
        // let tmp = hello;
        }
    );

    // Receivind the object from the channel
    let data = receiver.recv().unwrap();

    println!("{}", data);
}
