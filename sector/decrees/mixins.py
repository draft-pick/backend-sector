from rest_framework import mixins, viewsets


class CreateListDestroyModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет, который может создавать, возвращать и удалять список объектов.
    """
    pass
