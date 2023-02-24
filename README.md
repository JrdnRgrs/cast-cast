# Cast-Cast

This project was (at least initially) written (in part) by ChatGPT, since I had no idea what to do. Thanks!

The initial intent of this project was to allow me easily to stream audio of my turntable to a Cast enabled speaker in another part of my house. I will include details about the setup of that here, but this project really works with any icecast stream.

The whole point of this was to have it as just another Docker container running on my home server. This is by absolutely no means the best way of doing this, nor is it secure (probably) at all. But it works for what I wanted to do. 

Any input is greatly appreciated. If you want to make this look really cool, please do. I literally just asked ChatGPT for the CSS (make it look modern and sleek).

My dream would be to incorporate a music recognition service into this, or the icecast server even, to also have the song details of what is playing on the turntable. Would be nice to be able to cast this, or another page to something like a Google Nest Hub sitting next to the turntable so you have a live Now Playing screen. 

### Turntable Setup

The way I have things set up is a tad complicated and in no way ideal for everyone, but I will describe the whole setup for those who may benefit in the future.

- Raspberry Pi 4 - Home Server
  - This has a number of Docker containers running for various servers I maintain, one of which is an Icecast container that is listening for local streams on a specific port with a password.
  - The icecast stream is then made available to `my.domain/turntable` via CloudFlare tunnels (also Docker containers)
- Raspberry Pi Zero W - connected to home network, inside turntable cabinet with other audio equipment
  - USB Sound card connected via micro USB slot (Behringer U-Control UCA202)
    - RCA input is the output from the turntable, after the pre-amp
      - I used a set of RCA piggyback cables to intercept the audio without messing with the original audio
  - Runs darkice on boot and sends an audio stream from the USB card to the Icecast container's IP

All of that gives you a stream of whatever is playing on my turntable at `my.domain/turntable`, which is all we need for our initial intent.

## Usage

As a docker container, this must be run with host networking on (`net=host`). I also had a little trouble running the container on Windows but YMMV, as always with Docker on Windows.

Build the image:
```docker
docker build -t cast-cast .
```

Run the server:
```docker
docker run --net=host --name "cast-cast" -d cast-cast
```

You can now visit [localhost:5000](http://localhost:5000) to see the webpage.

1. Enter the stream URL.
2. Choose a device from the list of available Cast enabled devices on your network.
3. Click `Start Casting` to start casting to the device.
4. Click `Stop Casting` to stop casting to the device.

This would also technically work with a URL to an audio file as well, but if you try to use a youtube link and cast to an audio only device, you will likely hit an error.


### DISCLAIMER

This is not secure and is likely very unsecure. ChatGPT helped me write this when I just told it what I wanted. My specialtly is getting the code to the server, not the code itself. 

### Credits

- catt
- pychromecast
- ChatGPT