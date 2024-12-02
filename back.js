
    const inputField = document.querySelector("input");
    const downloadButton = document.querySelector("button");

    downloadButton.addEventListener("click", async function () {
        const videoURL = inputField.value.trim();

        if (!isValidURL(videoURL)) {
            alert("Please enter a valid YouTube video URL.");
            return;
        }

        try {
            const formatsResponse = await fetch('/formats', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: videoURL })
            });
            const formatsData = await formatsResponse.json();

            if (formatsResponse.ok) {
                const formats = formatsData.formats;
                const formatList = formats.map(f => `${f.format_id} - ${f.format_note} (${f.ext})`).join('\n');
                const selectedFormat = alert("Available formats:\n" + formatList + "\n\nEnter the format code to download:");

                if (selectedFormat) {
                    const savePath = prompt("Enter the save path (e.g., video.mp4):", "video.mp4");
                    
                    const downloadResponse = await fetch('/download', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ url: videoURL, format_code: selectedFormat, save_path: savePath })
                    });
                    const downloadData = await downloadResponse.json();

                    if (downloadResponse.ok) {
                        alert("Download successful! Saved to: " + downloadData.path);
                    } else {
                        alert("Download failed: " + downloadData.error);
                    }
                }
            } else {
                alert("Error fetching formats: " + formatsData.error);
            }
        } catch (error) {
            console.error(error);
            alert("An error occurred. Please try again.");
        }
    });


function isValidURL(url) {
    const youtubeRegex = /^(https?:\/\/)?(www\.)?(youtube\.com|youtu\.be)\/.+$/;
    return youtubeRegex.test(url);
}
