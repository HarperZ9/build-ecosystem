"""Tests for quanta-ecosystem — verify all packages are importable."""


class TestPackageImports:
    """Verify every package in the ecosystem is importable."""

    def test_quanta_color(self):
        import quanta_color

        assert quanta_color.__version__ == "1.0.0"

    def test_quanta_finance(self):
        from quanta_finance import indicators

        assert indicators is not None

    def test_quanta_oracle(self):
        from quanta_oracle import arima

        assert arima is not None

    def test_quanta_engine(self):
        from quanta_engine import adaptive_engine

        assert adaptive_engine is not None

    def test_calibrate_pro(self):
        from calibrate_pro.core import color_math

        assert color_math is not None

    def test_quanta_ui(self):
        from quanta_ui.theme import C

        assert C.ACCENT == "#d4a0a0"


class TestCrossWiring:
    """Verify cross-package dependencies work."""

    def test_calibrate_pro_uses_quanta_color(self):
        """calibrate-pro should delegate color math to quanta-color."""
        import numpy as np
        from calibrate_pro.core.color_math import srgb_to_xyz

        result = srgb_to_xyz(np.array([1.0, 0.0, 0.0]))
        assert result is not None
        assert len(result) == 3

    def test_engine_imports_oracle(self):
        from quanta_engine.model_trainer import ModelTrainer

        assert ModelTrainer is not None

    def test_engine_imports_finance(self):
        from quanta_engine.prediction_strategy import PredictionStrategy

        assert PredictionStrategy is not None


class TestEcosystemMeta:
    """Test the ecosystem meta-package itself."""

    def test_version(self):
        import quanta_ecosystem

        assert quanta_ecosystem.__version__ == "1.0.0"
