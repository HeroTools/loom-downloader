# Loom Video Downloader

A simple and effective Python tool for downloading videos from Loom. Built with `yt-dlp` for reliable video extraction and download capabilities.

## Features

- ✅ **URL Validation** - Automatically validates Loom video URLs
- ✅ **Multiple Quality Options** - Download in best, worst, video-only, or audio-only quality
- ✅ **Metadata Extraction** - Saves video info, thumbnails, and subtitles
- ✅ **Custom Output Directory** - Specify where to save downloaded content
- ✅ **Command-Line Interface** - Easy to use with command-line arguments
- ✅ **Error Handling** - Clear error messages and graceful failure handling

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Install Dependencies

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd loom-downloader
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Download a Loom video with default settings:
```bash
python loom_downloader.py "https://www.loom.com/share/your-video-id"
```

### Advanced Usage

**Custom output directory:**
```bash
python loom_downloader.py "https://www.loom.com/share/your-video-id" -o "/path/to/downloads"
```

**Specify video quality:**
```bash
python loom_downloader.py "https://www.loom.com/share/your-video-id" -q best
```

**Full example with all options:**
```bash
python loom_downloader.py "https://www.loom.com/share/abc123def456" -o "./my_videos" -q bestvideo
```

### Command-Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `url` | - | Loom video URL (required) | - |
| `--output` | `-o` | Output directory for downloads | `./downloads` |
| `--quality` | `-q` | Video quality selection | `best` |

### Quality Options

- `best` - Highest available quality (default)
- `worst` - Lowest available quality
- `bestvideo` - Best video quality (video only)
- `bestaudio` - Best audio quality (audio only)

## Supported URL Formats

The downloader supports various Loom URL formats:
- `https://www.loom.com/share/[video-id]`
- `https://loom.com/share/[video-id]` 
- `https://www.loom.com/embed/[video-id]`
- `https://loom.com/embed/[video-id]`

## Output Files

When downloading a video, the tool creates several files:

- **Video file** - The main video in the best available format
- **Thumbnail** - Video thumbnail image (`.jpg` or `.png`)
- **Info file** - Video metadata in JSON format (`.info.json`)
- **Subtitles** - Automatic and manual subtitles if available (`.srt`, `.vtt`)

## How It Works

1. **URL Validation** - Checks if the provided URL is a valid Loom video link
2. **Metadata Extraction** - Uses `yt-dlp` to extract video information without downloading
3. **Quality Selection** - Determines the best available format based on your quality preference  
4. **Download Process** - Downloads the video along with thumbnails, metadata, and subtitles
5. **File Organization** - Saves all files to your specified output directory

## Troubleshooting

### Common Issues

**"Invalid Loom URL provided"**
- Ensure the URL is a complete Loom video link
- Check that the video is publicly accessible or you have permission to view it

**"Error downloading video"**  
- The video may be private or restricted
- Check your internet connection
- Try updating yt-dlp: `pip install --upgrade yt-dlp`

**"Permission denied" errors**
- Make sure you have write permissions to the output directory
- Try running with elevated privileges if necessary

### Dependencies

If you encounter import errors, ensure all dependencies are installed:
```bash
pip install --upgrade yt-dlp
```

## Technical Details

- **Built with**: Python 3.9+
- **Core dependency**: yt-dlp (YouTube-DL fork)
- **Supported formats**: MP4, WebM, and other formats supported by yt-dlp
- **Platform compatibility**: Windows, macOS, Linux

## Contributing

This project is developed and maintained by **HeroTools**.

## Disclaimer

This tool is provided "as is" without warranty of any kind. HeroTools is not liable for any damages or issues arising from the use of this software. Users are responsible for ensuring they have proper permissions to download content and for complying with Loom's terms of service.

## License

MIT License - see [LICENSE](LICENSE) file for details.

This tool is for educational and personal use. Please respect Loom's terms of service and only download videos you have permission to access.

---

**Developed by HeroTools**