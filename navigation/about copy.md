---
layout: post
title: About
permalink: /about/
comments: true
---

### Coding progression

I started with scratch many years ago, where I remained for around 3 years.
There where sprinkles of JavaScript and Luau, but Scratch was the dominant coding language for me.

Eventually I moved on to C, and then Armv7 assembly.
I had a lot of fun with the Armv7 assembly, and it taught me alot about the inner workings of computers.

That about encompasses my experience in coding so far, minus a few projects here and there.

## Important places for me

Here are the 2 U.S. states I know where significant to my life, a long with the 2 countries of which I derive my heritage (Poland and Mexico).

<comment>
Flags are from Wikipedia images
</comment>

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }

    .image-gallery {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 10px;
        }

    .image-gallery img {
        max-height: 150px;
        object-fit: cover;
        border-radius: 5px;
    }
</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>

<script>
    var GRID_CONTAINER = document.getElementById("grid_container");

    var FLAGS = [
        {
            Name: "California", 
            Flag_Img: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_California.svg/1920px-Flag_of_California.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail&_=20251109150536"
        },
        {
            Name: "Arizona",
            Flag_Img: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag_of_Arizona.svg/1920px-Flag_of_Arizona.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail&_=20260122002829"
        },
        {
            Name: "Poland",
            Flag_Img: "https://upload.wikimedia.org/wikipedia/en/1/12/Flag_of_Poland.svg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original"
        },
        {
            Name: "Mexico",
            Flag_Img: "https://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Mexico.svg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
        }
    ];

    var FLAG_COUNT = 4;

    GRID_CONTAINER.style.border = "2px dashed";
    GRID_CONTAINER.style.padding = "8px";
    // GRID_CONTAINER.style.width = "512px";
    GRID_CONTAINER.style.height = "512px";

    GRID_CONTAINER.style.display = "grid";
    GRID_CONTAINER.style.gridTemplateColumns = "auto auto";
    GRID_CONTAINER.style.gridTemplateRows = "256px";

    for (var i = 0; i < FLAG_COUNT; i++) {
        var placeContainer = document.createElement("div");
        placeContainer.style.border = "2px dashed";
        placeContainer.style.padding = "8px"

        placeContainer.id = "placeContainer";

        var flagImage = document.createElement("img");
        flagImage.src = FLAGS[i].Flag_Img;
        flagImage.alt = FLAGS[i].Name;
        flagImage.objectFit = "contain";
        flagImage.style.width = "100%";
        flagImage.style.height = "90%";

        placeContainer.appendChild(flagImage);

        var textDiv = document.createElement("p");
        textDiv.style.textAlign = "center";
        textDiv.textContent = FLAGS[i].Name;

        placeContainer.appendChild(textDiv);

        GRID_CONTAINER.appendChild(placeContainer);
    }

    // Add containter to output 
    GRID_CONTAINER.appendChild(container);
</script>

---

<comment>
Here are some things I've worked on in the past. Some of them are in Blender, a 3D modeling software.

One of them is of a computer I was working on in Roblox Studio, although I have since stopped using the software
</comment>

<div class="image-gallery">
  <img src="{{site.baseurl}}/images/about/Screenshot 2026-07-05 211048.png" alt="Image 1">
  <img src="{{site.baseurl}}/images/about/Screenshot 2026-08-31 221312.png" alt="Image 2">
  <img src="{{site.baseurl}}/images/about/Screenshot 2026-08-31 221358.png" alt="Image 3">
  <img src="{{site.baseurl}}/images/about/Screenshot 2026-08-31 221417.png" alt="Image 4">
  <img src="{{site.baseurl}}/images/about/Screenshot 2025-12-25 154119.png" alt="Image 5">
</div>
