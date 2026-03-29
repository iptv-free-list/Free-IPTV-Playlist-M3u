# Aegis M3U: Advanced Free IPTV Playlist M3u Validator

Aegis M3U is an enterprise-grade, highly concurrent stream analyzer designed to strictly validate, sanitize, and verify the health of open-source and public-domain IPTV playlists.

[![Free IPTV Playlist M3u](https://raw.githubusercontent.com/iptv-free-list/Free-IPTV-Playlist-M3u/main/Free-IPTV-Playlist-M3u.png "Free IPTV Playlist M3u")](https://hakunatvip.com/)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![Version](https://img.shields.io/badge/version-v2.4.1-orange) ![Coverage](https://img.shields.io/badge/coverage-98%25-success)

## Table of Contents
1. [Overview](#overview)
2. [Core Architecture & Features](#core-architecture--features)
3. [Protocol Inspection](#protocol-inspection)
4. [Installation](#installation)
5. [Usage & CLI Arguments](#usage--cli-arguments)
6. [Diagnostic Output](#diagnostic-output)
7. [Compliance & Safety](#compliance--safety)

## Overview

Managing a reliable Free IPTV Playlist M3u can be a complex administrative bottleneck, especially when curating extensive manifests of over-the-air (OTA) broadcasts and globally accessible public-domain networks. Aegis M3U engineers a robust, programmatic solution by parsing playlist files, executing asynchronous deep-packet inspection on broadcast endpoints, and generating comprehensive diagnostic telemetry. 

Rather than relying on superficial HTTP status codes, Aegis M3U downloads stream chunks, verifies codec integrity, and maps geographic latency, ensuring that your public-domain playlists deliver a seamless viewing experience.

## Core Architecture & Features

Our validation engine is built with a focus on speed, accuracy, and network efficiency. 

*   **Asynchronous Probing Engine:** Utilizes non-blocking I/O multiplexing to concurrently ping hundreds of endpoints, drastically reducing parsing time for massive Free IPTV Playlist M3u files.
*   **Manifest Sanitization:** Automatically detects malformed `EXTM3U` tags, broken metadata, orphaned `#EXTINF` headers, and structural anomalies.
*   **Geographic Latency Mapping:** Measures Time-To-First-Byte (TTFB), jitter, and packet drop rates across various public-domain broadcast servers.
*   **Dead-Link Pruning:** Intelligently drops streams returning `404 Not Found`, `502 Bad Gateway`, or persistent timeout errors, exporting a clean, finalized `.m3u` file.

## Protocol Inspection

Aegis M3U natively supports advanced streaming protocols, allowing the engine to dissect manifest files and verify chunk continuity and adaptive bitrate integrity. 

For developers unfamiliar with the underlying architecture of these dynamic streams, we highly recommend reviewing this technical primer on the protocol: [https://www.cloudflare.com/learning/video/what-is-hls/](https://www.cloudflare.com/learning/video/what-is-hls/) to better understand the advanced validation metrics utilized by our tool. By understanding how the index files point to localized `.ts` (MPEG-2 Transport Stream) chunks, you can leverage Aegis M3U's strict timeline validation parameters effectively.

## Installation

Aegis M3U is designed to be lightweight and operates natively in any POSIX-compliant environment.

```bash
# Clone the repository
git clone https://github.com/aegis-validator/aegis-m3u.git

# Navigate to the project directory
cd aegis-m3u

# Install required dependencies
pip install -r requirements.txt
```

## Usage & CLI Arguments

Execute the validator via the command line. The tool requires an input playlist and offers various flags for granular control over the validation threshold.

```bash
python aegis.py --input public_streams.m3u --output verified_streams.m3u --threads 50 --timeout 5000
```

### Argument Glossary
*   `--input`: (Required) Path to your local Free IPTV Playlist M3u file.
*   `--output`: Path to save the sanitized, fully verified playlist.
*   `--threads`: Number of concurrent worker threads (Default: 20).
*   `--timeout`: Maximum connection timeout in milliseconds before flagging a stream as dead.
*   `--strict-codec`: Forces FFmpeg probe to verify audio/video codec metadata (slower, but highly accurate).

## Diagnostic Output

Upon completion, Aegis M3U generates a machine-readable JSON telemetry report detailing the health of your list.

```json
{
  "total_streams_parsed": 1250,
  "active_streams": 1102,
  "dead_streams": 148,
  "average_latency_ms": 142,
  "sample_validation": {
    "stream_id": "ota_public_broadcasting_01",
    "status": "HEALTHY",
    "codec": "H.264/MPEG-4 AVC",
    "resolution": "1920x1080",
    "packet_loss_pct": 0.01
  }
}
```

## Compliance & Safety

**Strict Acceptable Use Policy:** Aegis M3U is strictly a network diagnostic utility. It is engineered explicitly for testing, validating, and maintaining playlists consisting solely of free, public-domain, and over-the-air (OTA) networks. 

We strictly prohibit the use of this tool for validating unauthorized, copyrighted, or pirated material. The developers of Aegis M3U do not host, index, or distribute any media streams. Ensure all endpoints passed through this validator adhere strictly to local broadcast regulations and safe harbor guidelines.

---

[![Free IPTV Playlist M3u](https://raw.githubusercontent.com/iptv-free-list/Free-IPTV-Playlist-M3u/main/Free-IPTV-Playlist-M3u.png "Free IPTV Playlist M3u")](https://hakunatvip.com/)