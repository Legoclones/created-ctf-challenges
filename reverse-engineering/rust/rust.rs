use std::io;

fn main() {
    let mut flag = String::new();
    io::stdin().read_line(&mut flag).expect("Failed to read line");

    if flag.len() != 25 {
        return;
    }

    let chars: Vec<char> = flag.trim().chars().collect();

    let numbers = [167, 190, 186, 168, 185, 171, 192, 183, 186, 184, 185, 164, 172, 180, 164, 167, 183, 183, 183, 183, 183, 183, 183, 194];

    for i in 0..24 {
        let result = (chars[i] as u8) as i32 + 69;

        if numbers[i] != result {
            return;
        }
    }

    println!("Correct!");
}