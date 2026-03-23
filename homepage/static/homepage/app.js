document.addEventListener('DOMContentLoaded', function () {
  const titleInput = document.querySelector('#id_title');
  const captionInput = document.querySelector('#id_caption');
  const previewTitle = document.querySelector('#preview-title');
  const previewCaption = document.querySelector('#preview-caption');

  if (titleInput && captionInput && previewTitle && previewCaption) {
    const updatePreview = () => {
      previewTitle.textContent = titleInput.value.trim() || '(Title will appear here)';
      previewCaption.textContent = captionInput.value.trim() || '(Your words will appear here)';
    };

    titleInput.addEventListener('input', updatePreview);
    captionInput.addEventListener('input', updatePreview);
    updatePreview();
  }

  function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      const [key, value] = cookie.trim().split('=');
      if (key === name) {
        return decodeURIComponent(value);
      }
    }
    return null;
  }

  const csrfToken = getCookie('csrftoken');

  document.querySelectorAll('.candle-btn').forEach((button) => {
    button.addEventListener('click', (event) => {
      event.preventDefault();
      const postId = button.dataset.postId;

      if (!postId) {
        return;
      }

      fetch(`/candle/${encodeURIComponent(postId)}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
      })
        .then((res) => {
          if (!res.ok) {
            throw new Error('Network response was not OK');
          }
          return res.json();
        })
        .then((data) => {
          const countEl = document.querySelector(`#candle-count-${postId}`);
          if (countEl && data.candle_count !== undefined) {
            countEl.textContent = data.candle_count;
          }
        })
        .catch((err) => {
          console.error('Failed to update candle count:', err);
          alert('Could not light a candle right now. Please try again.');
        });
    });
  });
});
