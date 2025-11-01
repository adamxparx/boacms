(function() {
    const MIN = "09:00";
    const MAX = "16:30";

    function setConstraints() {
      const timeInputs = document.querySelectorAll('input[type="time"], input[name$="appointment_time"]');
      timeInputs.forEach(inp => {
        try { inp.min = MIN; inp.max = MAX; } catch(e) {}
        inp.addEventListener('change', () => validateTime(inp));
        inp.addEventListener('input', () => inp.setCustomValidity(''));
      });
    }

    function parseTime(val) {
      if (!val) return null;
      const parts = val.split(":").map(Number);
      if (parts.length < 2) return null;
      return parts[0] * 60 + parts[1];
    }

    function validateTime(input) {
      const v = parseTime(input.value);
      const min = parseTime(MIN);
      const max = parseTime(MAX);
      if (v == null) return true;
      if (v < min || v > max) {
        input.setCustomValidity(`Please select a time between ${MIN} and ${MAX}.`);
        input.reportValidity();
        return false;
      } else {
        input.setCustomValidity('');
        return true;
      }
    }

    function attachFormGuards() {
      const forms = document.querySelectorAll('.auth-form, .cert');
      forms.forEach(form => {
        form.addEventListener('submit', (e) => {
          const timeInputs = form.querySelectorAll('input[type="time"], input[name$="appointment_time"]');
          let ok = true;
          timeInputs.forEach(inp => { if (!validateTime(inp)) ok = false; });
          if (!ok) {
            e.preventDefault();
          }
        });
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      setConstraints();
      attachFormGuards();
    });
  })();