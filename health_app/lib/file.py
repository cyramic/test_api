import logging

from fs import open_fs

log = logging.getLogger(__name__)


def get_temp_fs(upload_dir):
    """
    Gets a reference to the temporary storage location

    Parameters:
    upload_dir: A FS_URL to the upload folder

    Returns:
    filesystem reference
    """
    try:
        # Open local filesystem with the upload directory path
        file_fs = open_fs(upload_dir)
        log.info(file_fs)
    except Exception as err:
        log.error(f"Upload Directory not accessible {err}")
        return False
    return file_fs
