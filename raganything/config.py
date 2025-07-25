"""
Configuration classes for RAGAnything

Contains configuration dataclasses with environment variable support
"""

from dataclasses import dataclass, field
from typing import List
from lightrag.utils import get_env_value


@dataclass
class RAGAnythingConfig:
    """Configuration class for RAGAnything with environment variable support"""

    # Directory Configuration
    # ---
    working_dir: str = field(default=get_env_value("WORKING_DIR", "./rag_storage", str))
    """Directory where RAG storage and cache files are stored."""

    # MinerU Parser Configuration
    # ---
    mineru_parse_method: str = field(
        default=get_env_value("MINERU_PARSE_METHOD", "auto", str)
    )
    """Default parsing method for MinerU: 'auto', 'ocr', or 'txt'."""

    mineru_output_dir: str = field(
        default=get_env_value("MINERU_OUTPUT_DIR", "./output", str)
    )
    """Default output directory for MinerU parsed content."""

    display_content_stats: bool = field(
        default=get_env_value("DISPLAY_CONTENT_STATS", True, bool)
    )
    """Whether to display content statistics during parsing."""

    # Multimodal Processing Configuration
    # ---
    enable_image_processing: bool = field(
        default=get_env_value("ENABLE_IMAGE_PROCESSING", True, bool)
    )
    """Enable image content processing."""

    enable_table_processing: bool = field(
        default=get_env_value("ENABLE_TABLE_PROCESSING", True, bool)
    )
    """Enable table content processing."""

    enable_equation_processing: bool = field(
        default=get_env_value("ENABLE_EQUATION_PROCESSING", True, bool)
    )
    """Enable equation content processing."""

    # Batch Processing Configuration
    # ---
    max_concurrent_files: int = field(
        default=get_env_value("MAX_CONCURRENT_FILES", 1, int)
    )
    """Maximum number of files to process concurrently."""

    supported_file_extensions: List[str] = field(
        default_factory=lambda: get_env_value(
            "SUPPORTED_FILE_EXTENSIONS",
            ".pdf,.jpg,.jpeg,.png,.bmp,.tiff,.tif,.gif,.webp,.doc,.docx,.ppt,.pptx,.xls,.xlsx,.txt,.md",
            str,
        ).split(",")
    )
    """List of supported file extensions for batch processing."""

    recursive_folder_processing: bool = field(
        default=get_env_value("RECURSIVE_FOLDER_PROCESSING", True, bool)
    )
    """Whether to recursively process subfolders in batch mode."""

    # Context Extraction Configuration
    # ---
    context_window: int = field(default=get_env_value("CONTEXT_WINDOW", 1, int))
    """Number of pages/chunks to include before and after current item for context."""

    context_mode: str = field(default=get_env_value("CONTEXT_MODE", "page", str))
    """Context extraction mode: 'page' for page-based, 'chunk' for chunk-based."""

    max_context_tokens: int = field(
        default=get_env_value("MAX_CONTEXT_TOKENS", 2000, int)
    )
    """Maximum number of tokens in extracted context."""

    include_headers: bool = field(default=get_env_value("INCLUDE_HEADERS", True, bool))
    """Whether to include document headers and titles in context."""

    include_captions: bool = field(
        default=get_env_value("INCLUDE_CAPTIONS", True, bool)
    )
    """Whether to include image/table captions in context."""

    context_filter_content_types: List[str] = field(
        default_factory=lambda: get_env_value(
            "CONTEXT_FILTER_CONTENT_TYPES", "text", str
        ).split(",")
    )
    """Content types to include in context extraction (e.g., 'text', 'image', 'table')."""

    content_format: str = field(default=get_env_value("CONTENT_FORMAT", "minerU", str))
    """Default content format for context extraction when processing documents."""
