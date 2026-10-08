# oogitdiff: Sovereign Git Tree Differ

<div align="center">

```
================================================================================
                                oogitdiff
               Sovereign openOODA Git Tree Differ & Engine
================================================================================
```

**Sovereign Git Tree Differ**  
*Fast working tree vs commit object differ without requiring ambient git porcelain.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oogitdiff/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oogitdiff-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oogitdiff/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oogitdiff/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oogitdiff-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oogitdiff/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oogitdiff [options] [<commit>] [--] [<path>...]

Fast working tree vs commit object differ without requiring ambient git porcelain.

Options:
  -h, --help           display this help and exit
  -v, --version        output version information and exit
      --staged, --cached   view changes staged for the next commit
      --stat           generate a diffstat summary instead of patch
  -s, --name-status    show only names and status of changed files
  -p, --patch          generate diff in patch format (default)
  -j, --json           output structured JSON metrics
  -D, --demo           interactive simulated git delta showcase
      --no-color       suppress ANSI color escape sequences
      --test           execute internal multi-tier verification suite
      --mcp            run as Model Context Protocol stdio server
```

---

## 3. Theming Integration (`oote`)

`oogitdiff` synchronizes visual styles and diff colors with [oote](https://github.com/openOODA-tools/oote):
* **Colors:** Green for additions, Red for deletions, Cyan for hunk headers (`@@ -o,c +n,c @@`).
* **Environment Overrides:** Respects `$OODA_THEME` and suppresses color under `$NO_COLOR` or `--no-color`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oogitdiff` runs a JSON-RPC 2.0 stdio server providing 5 tools for AI coding agents:

1. `gitdiff_status`: Query modified, added, deleted, and untracked file status.
2. `gitdiff_diff`: Generate standard unified diff patch for working tree or specific files.
3. `gitdiff_stat`: Calculate line addition/deletion diffstats and histogram bar.
4. `gitdiff_tree`: Compare commit revisions or branches.
5. `gitdiff_demo`: Run multi-scenario simulated git repository delta showcase.

```bash
oogitdiff --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`, `&McpCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation, bounded loops, and fail-closed evaluation.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
