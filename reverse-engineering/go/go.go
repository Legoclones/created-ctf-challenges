package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"math/rand"
	"strconv"
)

func GetMD5Hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}

func main() {
	fmt.Print("Password: ")

	var password string

	fmt.Scanln(&password)

	hash := GetMD5Hash(password)

	var correct = "27443509682471009008637982892046"

	if hash == correct {
		intVar, err := strconv.Atoi(hash)
		if err != nil {
		}
		rand.Seed(int64(intVar))

		var flag string
		var some_bytes = []byte{0x41, 0x2a, 0x34, 0x44, 0x2f, 0x6e, 0x74, 0x35, 0x61, 0x79, 0x57, 0x46, 0x5f, 0x35, 0x6f, 0x7e, 0x2c, 0x4c, 0x3a, 0x24, 0x50, 0x4b, 0x70, 0x71}

		for i := 0; i < 24; i++ {
			flag += string(rand.Intn(94) ^ int(some_bytes[i]))
		}

		fmt.Println("Flag: " + flag)
	} else {
		fmt.Println("Wrong!")
	}
}
