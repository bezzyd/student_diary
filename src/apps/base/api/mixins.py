from rest_framework.serializers import Serializer


class SerializerPerActionMixin:
    action: str
    serializer_class: Serializer | None
    action_serializer: dict[str, Serializer]

    def get_serializer_class(self):
        assert getattr(self, "action_serializer", None) is not None, (
            "'%s' should either include a `action_serializer` attribute, "
            "or override the `get_serializer_class()` method." % self.__class__.__name__
        )

        assert "default" in self.action_serializer, "..."

        self.serializer_class = self.action_serializer.get(
            self.action, self.action_serializer["default"]
        )
        return super().get_serializer_class()
