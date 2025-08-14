#!/usr/bin/env python3

import os
import re
import sys
import argparse
from pathlib import Path
import yt_dlp


class LoomDownloader:
    def __init__(self, output_dir="./downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def is_valid_loom_url(self, url):
        """Validate if the URL is a valid Loom video URL"""
        loom_patterns = [
            r'https?://(?:www\.)?loom\.com/share/[a-zA-Z0-9]+',
            r'https?://(?:www\.)?loom\.com/embed/[a-zA-Z0-9]+',
            r'https?://(?:.*\.)?loom\.com/.*'
        ]
        return any(re.match(pattern, url) for pattern in loom_patterns)
    
    def download_video(self, url, quality='best'):
        """Download Loom video using yt-dlp"""
        if not self.is_valid_loom_url(url):
            raise ValueError("Invalid Loom URL provided")
        
        ydl_opts = {
            'format': quality,
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'writeinfojson': True,
            'writethumbnail': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'ignoreerrors': False,
            'extractflat': False,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading from: {url}")
                print(f"Output directory: {self.output_dir}")
                
                info = ydl.extract_info(url, download=False)
                if info:
                    print(f"Title: {info.get('title', 'Unknown')}")
                    print(f"Duration: {info.get('duration', 'Unknown')} seconds")
                    print(f"Uploader: {info.get('uploader', 'Unknown')}")
                
                ydl.download([url])
                print("✓ Download completed successfully!")
                
        except Exception as e:
            print(f"✗ Error downloading video: {str(e)}")
            raise


def main():
    parser = argparse.ArgumentParser(description='Download Loom videos')
    parser.add_argument('url', help='Loom video URL')
    parser.add_argument('-o', '--output', default='./downloads', 
                       help='Output directory (default: ./downloads)')
    parser.add_argument('-q', '--quality', default='best',
                       choices=['best', 'worst', 'bestvideo', 'bestaudio'],
                       help='Video quality (default: best)')
    
    args = parser.parse_args()
    
    try:
        downloader = LoomDownloader(args.output)
        downloader.download_video(args.url, args.quality)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()